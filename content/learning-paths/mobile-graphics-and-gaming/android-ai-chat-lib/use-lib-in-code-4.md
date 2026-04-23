---
title: Implement the main activity logic
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Implement MainActivity

Implement the app logic in `MainActivity.kt` to use the AI Chat library for LLM interaction.

First, replace the default imports with the following:
```kotlin
import android.os.Bundle
import android.net.Uri
import android.provider.OpenableColumns
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.arm.aichat.AiChat
import com.arm.aichat.InferenceEngine
import com.google.android.material.button.MaterialButton
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.onCompletion
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.io.File
import java.io.IOException
import java.util.UUID
import kotlin.math.max
```

## Define class variables

Within the `MainActivity` class, define all the class variables needed for UI components and AI Chat functionality:
```kotlin
class MainActivity : AppCompatActivity() {
    private lateinit var rootView: androidx.constraintlayout.widget.ConstraintLayout    // Root layout used to apply resizing.
    private lateinit var statusText: TextView    // Status label that reports engine and model state.
    private lateinit var messagesView: RecyclerView    // Message list showing the chat history.
    private lateinit var userInput: EditText    // Text box for the user's prompt.
    private lateinit var sendButton: MaterialButton    // Button that imports a model first, then sends prompts.

    private lateinit var engine: InferenceEngine    // Single ai-chat engine instance for the activity.

    private val messages = mutableListOf<Message>()    // Backing list for chat messages.
    private val adapter = MessageAdapter(messages)    // RecyclerView adapter bound to the message list.
    private val lastAssistantMessage = StringBuilder()    // Buffer used while assistant tokens stream in.

    private var modelReady = false    // Tracks whether a model has finished loading.
    private var sending = false    // Prevents overlapping prompt submissions.
    private var loadedModelName = "chat.gguf"    // Remembers the original imported filename for status text.
```

## Implement model loading

Add the model loading logic that copies the selected GGUF model file to local storage and loads it into the inference engine:
    // Fixed local destination for the copied model file.
    private val importedModelFile: File
        get() = File(ensureModelsDirectory(), "chat.gguf")

    // One-time file picker used to import a GGUF from device storage.
    private val importModel = registerForActivityResult(
        ActivityResultContracts.OpenDocument()
    ) { uri ->
        uri?.let { handleSelectedModel(it) }
    }

    private fun handleSelectedModel(uri: Uri) {
        sendButton.isEnabled = false
        statusText.text = "Copying selected model..."

        lifecycleScope.launch {
            try {
                loadedModelName = resolveDisplayName(uri)
                val modelFile = copySelectedModel(uri)

                statusText.text = "Loading model: $loadedModelName"
                withContext(Dispatchers.IO) {
                    engine.loadModel(modelFile.absolutePath)
                }

                modelReady = true
                userInput.isEnabled = true
                userInput.hint = "Ask something"
                sendButton.isEnabled = true
                sendButton.text = "Send"
                statusText.text = "Model ready: $loadedModelName"
            } catch (t: Throwable) {
                sendButton.isEnabled = true
                statusText.text = "Failed to import model $loadedModelName: ${t.message ?: t::class.java.simpleName}"
                Toast.makeText(this@MainActivity, "Model import failed", Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun resolveDisplayName(uri: Uri): String {
        contentResolver.query(uri, arrayOf(OpenableColumns.DISPLAY_NAME), null, null, null)
            ?.use { cursor ->
                val nameIndex = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME)
                if (nameIndex >= 0 && cursor.moveToFirst()) {
                    return cursor.getString(nameIndex)
                }
            }

        return uri.lastPathSegment ?: "chat.gguf"
    }

    private suspend fun copySelectedModel(uri: Uri): File =
        withContext(Dispatchers.IO) {
            val targetFile = importedModelFile

            contentResolver.openInputStream(uri)?.use { input ->
                targetFile.outputStream().use { output ->
                    input.copyTo(output)
                }
            } ?: throw IOException("Unable to open selected model file")

            targetFile
        }

    // Ensures the private model directory exists before copying the file.
    private fun ensureModelsDirectory(): File =
        File(filesDir, "models").also { directory ->
            if (directory.exists() && !directory.isDirectory) {
                directory.delete()
            }
            if (!directory.exists()) {
                directory.mkdirs()
            }
        }
```

## Initialize the app

Add the functions for creating and initializing the app UI and inference engine:
```kotlin
    // Wires the UI and prepares the engine for model import.
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        rootView = findViewById(R.id.root)
        statusText = findViewById(R.id.status_text)
        messagesView = findViewById(R.id.messages)
        userInput = findViewById(R.id.user_input)
        sendButton = findViewById(R.id.send_button)

        applyWindowInsets()

        messagesView.layoutManager = LinearLayoutManager(this)
        messagesView.adapter = adapter

        sendButton.setOnClickListener {
            if (modelReady) {
                sendCurrentPrompt()
            } else {
                importModel.launch(arrayOf("*/" + "*"))
            }
        }

        initializeEngine()
    }

    // Creates the inference engine and enables the initial import flow.
    private fun initializeEngine() {
        lifecycleScope.launch {
            statusText.text = "Creating inference engine..."

            try {
                engine = withContext(Dispatchers.Default) {
                    AiChat.getInferenceEngine(applicationContext)
                }
                sendButton.isEnabled = true
                userInput.hint = "Import a model first"
                statusText.text = "Choose a GGUF model from Downloads"
            } catch (t: Throwable) {
                statusText.text = "Failed to create engine: ${t.message ?: t::class.java.simpleName}"
            }
        }
    }
```

## Handle chat messaging

Implement the chat messaging logic that sends user prompts to the LLM and streams the response tokens back to the UI:
```kotlin
    // Sends the current prompt and streams the assistant response into the last row.
    private fun sendCurrentPrompt() {
        val prompt = userInput.text.toString().trim()
        if (!modelReady || sending || prompt.isEmpty()) {
            return
        }

        userInput.text?.clear()
        userInput.isEnabled = false
        sendButton.isEnabled = false
        sending = true

        messages.add(Message(UUID.randomUUID().toString(), prompt, true))
        adapter.notifyItemInserted(messages.lastIndex)
        messagesView.scrollToPosition(messages.lastIndex)

        lastAssistantMessage.clear()
        messages.add(Message(UUID.randomUUID().toString(), "", false))
        adapter.notifyItemInserted(messages.lastIndex)
        messagesView.scrollToPosition(messages.lastIndex)

        lifecycleScope.launch(Dispatchers.Default) {
            try {
                engine.sendUserPrompt(prompt)
                    .onCompletion {
                        withContext(Dispatchers.Main) {
                            sending = false
                            userInput.isEnabled = true
                            sendButton.isEnabled = true
                        }
                    }
                    .collect { token ->
                        val assistantIndex = messages.lastIndex
                        val updatedMessage = messages[assistantIndex].copy(
                            content = lastAssistantMessage.append(token).toString()
                        )
                        messages[assistantIndex] = updatedMessage

                        withContext(Dispatchers.Main) {
                            adapter.notifyItemChanged(assistantIndex)
                            messagesView.scrollToPosition(assistantIndex)
                        }
                    }
            } catch (t: Throwable) {
                val assistantIndex = messages.lastIndex
                messages[assistantIndex] = messages[assistantIndex].copy(
                    content = "Error: ${t.message ?: t::class.java.simpleName}"
                )

                withContext(Dispatchers.Main) {
                    adapter.notifyItemChanged(assistantIndex)
                    sending = false
                    userInput.isEnabled = true
                    sendButton.isEnabled = true
                }
            }
        }
    }

    // Applies padding for system bars and the on-screen keyboard.
    private fun applyWindowInsets() {
        ViewCompat.setOnApplyWindowInsetsListener(rootView) { view, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            val ime = insets.getInsets(WindowInsetsCompat.Type.ime())

            view.setPadding(
                systemBars.left,
                systemBars.top,
                systemBars.right,
                max(systemBars.bottom, ime.bottom)
            )

            insets
        }
    }
```

## Clean up resources

Add the cleanup function to release native resources when the activity is destroyed:
```kotlin
    // Releases native resources when the activity is destroyed.
    override fun onDestroy() {
        if (::engine.isInitialized) {
            engine.destroy()
        }
        super.onDestroy()
    }
```

The `MainActivity` class now contains all the logic needed to load models, send prompts, and display streamed responses. In the next section, you'll download a model and run the app on your device.
