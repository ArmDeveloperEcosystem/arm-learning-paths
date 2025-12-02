---
title: Building the Android Agent
weight: 10 
layout: learningpathall
---

## Overview
Now we will build the Android App that hosts our Agent. The core logic involves:
1.  **ModelRunner**: A wrapper around ExecuTorch to handle inference.
2.  **ToolRegistry**: A collection of Kotlin functions (Tools) the Agent can call.
3.  **AgentOrchestrator**: The loop that sends prompts, parses "Actions", executes tools, and loops back.

## 1. Project Setup
Create a new Android Project (Kotlin) and add the ExecuTorch dependencies as described in the previous steps.

## 2. The Tool Registry
Create a class to define what your Agent can *do*.

```kotlin
// ToolRegistry.kt
class ToolRegistry(private val context: Context) {

    fun execute(command: String): String {
        // Parse "ACTION: tool_name(args)"
        val toolName = command.substringAfter("ACTION: ").substringBefore("(")
        
        return when (toolName) {
            "check_battery_status" -> getBatteryStatus()
            "check_order_status" -> "Order #12345 is Out for Delivery." // Mock
            else -> "Error: Tool not found."
        }
    }

    private fun getBatteryStatus(): String {
        val bm = context.getSystemService(Context.BATTERY_SERVICE) as BatteryManager
        val level = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
        return "Battery Level is $level%."
    }
}
```

## 3. The Model Runner
This class handles the raw interaction with the `.pte` model.

```kotlin
// ModelRunner.kt
class ModelRunner(private val modelPath: String, private val tokenizerPath: String) {
    // ... Initialize ExecuTorch Module ...

    fun generate(prompt: String): String {
        // 1. Tokenize Prompt
        // 2. Run Inference (Module.forward)
        // 3. Decode Output Tokens
        return decodedResponse
    }
}
```
*Note: You can use the `LlamaRunner` from the ExecuTorch demo as a base for this.*

## 4. The Agent Orchestrator (The Loop)
This is where the magic happens. We intercept the model's output to check for actions.

```kotlin
// AgentOrchestrator.kt
class AgentOrchestrator(
    private val modelRunner: ModelRunner,
    private val toolRegistry: ToolRegistry
) {
    private val systemPrompt = """
        <|start_header_id|>system<|end_header_id|>
        You are a helpful Assistant.
        Tools: check_battery_status, check_order_status.
        Output ONLY: ACTION: tool_name() if needed.
        <|eot_id|>
    """.trimIndent()

    private var conversationHistory = systemPrompt

    suspend fun chat(userMessage: String): String {
        // 1. Append User Message
        conversationHistory += "<|start_header_id|>user<|end_header_id|>\n$userMessage<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"

        // 2. First Pass: Ask the Model
        var response = modelRunner.generate(conversationHistory)

        // 3. Check for Action
        if (response.contains("ACTION:")) {
            val toolResult = toolRegistry.execute(response)
            
            // 4. Feed Result back to Model
            conversationHistory += "$response\n<|start_header_id|>tool<|end_header_id|>\n$toolResult<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"
            
            // 5. Second Pass: Get Final Answer
            response = modelRunner.generate(conversationHistory)
        }

        conversationHistory += response
        return response
    }
}
```

## 5. UI Integration
In your `MainActivity`, simply call `agentOrchestrator.chat(userInput)`.

```kotlin
// MainActivity.kt
val agent = AgentOrchestrator(modelRunner, ToolRegistry(this))

sendButton.setOnClickListener {
    val input = inputBox.text.toString()
    lifecycleScope.launch {
        val reply = agent.chat(input)
        chatAdapter.addMessage(reply)
    }
}
```

## Summary
You now have an Android app where the LLM can "press buttons" (call functions) on the device!