---
# User change
title: "Define the UI"

weight: 4

layout: "learningpathall"
---
You will now define the application UI. 

## Modify the application view
To modify the application view, open `activity_main.xml` and replace the file contents with the following code:

```XML
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <LinearLayout
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:padding="16dp"
        android:gravity="center">

        <!-- Image View for the loaded and processed image -->
        <ImageView
            android:id="@+id/imageView"
            android:layout_width="match_parent"
            android:layout_height="300dp"
            android:layout_gravity="center"
            android:adjustViewBounds="true"
            android:scaleType="fitCenter"
            android:contentDescription="Image Preview" />

        <!-- Load Image Button -->
        <Button
            android:id="@+id/buttonLoadImage"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Load Image"
            android:layout_marginTop="16dp"
            android:layout_gravity="center"
            android:textColor="@android:color/white"
            android:elevation="4dp" />

        <!-- Spinner for Image Processing Selection -->
        <Spinner
            android:id="@+id/spinnerOperation"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="16dp"
            android:layout_gravity="center"
            android:spinnerMode="dropdown" />

        <!-- Process Button -->
        <Button
            android:id="@+id/buttonProcess"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Process"
            android:layout_marginTop="16dp"
            android:layout_gravity="center"
            android:elevation="4dp" />

        <!-- Text View to Display Computation Time -->
        <TextView
            android:id="@+id/textViewTime"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center"
            android:layout_marginTop="16dp"
            android:text="Time: "
            android:textSize="18sp" />

    </LinearLayout>

</androidx.constraintlayout.widget.ConstraintLayout>
```

This XML layout defines the user interface (UI) for an Android application. The root layout is a ConstraintLayout. Within the ConstraintLayout, a LinearLayout is embedded as the primary container for the UI components. This LinearLayout is oriented vertically, ensuring that its child elements are stacked one below the other. 

Inside the LinearLayout, the following components are defined:
1.	ImageView for Displaying Images. We will use it to display an original and processed image.
2.	Load Image Button. We use this button to load an image.
3.	Spinner for Selecting Image Processing Options.	
4.	Process Button. Another Button, which will trigger the image processing.	
5.	TextView to display computation time.

In the next step, you will implement the application logic.