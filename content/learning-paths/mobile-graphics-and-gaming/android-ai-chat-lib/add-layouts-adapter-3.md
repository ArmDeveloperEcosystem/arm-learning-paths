---
title: Add UI Code
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add Layouts
Currently the `activity_main.xml` layout file in your `app\src\main\res\layout` directory is nearly empty, containing just a "Hello World!" piece of text that we wish to remove. Instead, replace it with the following, which will create a status area at the top, a place for messages in the middle, and a place for you to type at the bottom with a button to send:
```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/root"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/status_text"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_marginStart="16dp"
        android:layout_marginTop="16dp"
        android:layout_marginEnd="16dp"
        android:text="Loading model..."
        android:textAppearance="@style/TextAppearance.MaterialComponents.Body1"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/messages"
        android:layout_width="0dp"
        android:layout_height="0dp"
        android:layout_marginStart="16dp"
        android:layout_marginTop="12dp"
        android:layout_marginEnd="16dp"
        android:clipToPadding="false"
        android:paddingBottom="8dp"
        app:layout_constraintBottom_toTopOf="@+id/input_row"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/status_text" />

    <LinearLayout
        android:id="@+id/input_row"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_margin="16dp"
        android:orientation="horizontal"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent">
        <EditText
            android:id="@+id/user_input"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:enabled="false"
            android:hint="Model is loading..."
            android:inputType="textMultiLine"
            android:maxLines="4"
            android:minHeight="48dp"
            android:padding="12dp" />
        <com.google.android.material.button.MaterialButton
            android:id="@+id/send_button"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginStart="12dp"
            android:enabled="false"
            android:text="Import model" />
    </LinearLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```

We also need two small "helper" layouts to format the messages from the user and the AI assistant. In the `layout` folder alongside the main layout, first create `item_message_user.xml` and insert the following:
```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:paddingTop="6dp"
    android:paddingBottom="6dp">

    <TextView
        android:id="@+id/msg_content"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="end"
        android:background="#D7F0FF"
        android:padding="12dp"
        android:textAppearance="@style/TextAppearance.MaterialComponents.Body1" />
</FrameLayout>
```

Then create `item_message_assistant.xml` and put the following as its contents:
```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:paddingTop="6dp"
    android:paddingBottom="6dp">

    <TextView
        android:id="@+id/msg_content"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="start"
        android:background="#EFEFEF"
        android:padding="12dp"
        android:textAppearance="@style/TextAppearance.MaterialComponents.Body1" />
</FrameLayout>
```

## Add the MessageAdaptor class
As a final bit of UI code, we add a `MessageAdapter.kt` code file to put our messages into the correct bit of layout. The file should sit alongside the `MainActivity` class that is auto-created with the project.

{{% notice Package name %}}
The `package` name below has to match that of your project name. If you named your project `simpleaichat`, you can copy the block without changes. If you named your project differently as you started out this Learning Path, make sure you update it after populating the file.
{{% /notice %}}

The file contents of `MessageAdapter.kt` are:

```kotlin
package com.example.simpleaichat

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

data class Message(
    val id: String,
    val content: String,
    val isUser: Boolean
)

class MessageAdapter(
    private val messages: List<Message>
) : RecyclerView.Adapter<RecyclerView.ViewHolder>() {

    override fun getItemViewType(position: Int): Int {
        return if (messages[position].isUser) VIEW_TYPE_USER else VIEW_TYPE_ASSISTANT
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        return if (viewType == VIEW_TYPE_USER) {
            UserMessageViewHolder(inflater.inflate(R.layout.item_message_user, parent, false))
        } else {
            AssistantMessageViewHolder(inflater.inflate(R.layout.item_message_assistant, parent, false))
        }
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        holder.itemView.findViewById<TextView>(R.id.msg_content).text = messages[position].content
    }

    override fun getItemCount(): Int = messages.size

    class UserMessageViewHolder(view: View) : RecyclerView.ViewHolder(view)
    class AssistantMessageViewHolder(view: View) : RecyclerView.ViewHolder(view)

    companion object {
        private const val VIEW_TYPE_USER = 1
        private const val VIEW_TYPE_ASSISTANT = 2
    }
}
```

Quickly going through the important parts:
- `Message` is the smallest useful chat piece: one id, the message text, and a flag saying whether it came from the user or the assistant.
- `getItemViewType(...)` decides which row layout to use for each message.
- `onCreateViewHolder(...)` inflates either the user bubble or the assistant bubble layout.
- `onBindViewHolder(...)` writes the current message text into the row.
- `getItemCount()` tells the `RecyclerView` how many chat rows it should render.
