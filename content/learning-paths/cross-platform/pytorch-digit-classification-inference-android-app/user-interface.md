---
# User change
title: "Create an Android App"

weight: 3

layout: "learningpathall"
---

In this section you will create an Android App to run digit classifier. The application will load a randomly selected image containing a handwritten digit, and its true label. Then you will be able to run an inference on this image to predict the digit. 

Start by creating a project and an user interface:
1. Open Android Studio and create a new project with an “Empty Views Activity.”
2. Set the project name to **ArmPyTorchMNISTInference**, set the package name to: **com.arm.armpytorchmnistinference**, select **Kotlin** as the language, and set the minimum SDK to **API 27 ("Oreo" Android 8.1)**.

We set the API to Android 8.1 (API level 27) as it introduced NNAPI, providing a standard interface for running computationally intensive machine learning models on Android devices. Devices with ARM-based SoCs and corresponding hardware accelerators can leverage NNAPI to offload ML tasks to specialized hardware, such as NPUs (Neural Processing Units), DSPs (Digital Signal Processors), or GPUs (Graphics Processing Units).

## User interface
You will design the user interface to contain the following:
1. A header.
2. An ImageView and TextView to display the image and its true label.
3. A button to load the image.
4. A button to run inference.
5. Two TextView controls to display the predicted label and inference time.

To do so, replace the contents of activity_main.xml (located under src/main/res/layout) with the following code:

```XML
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    android:gravity="center">

    <!-- Header -->
    <TextView
        android:id="@+id/header"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Digit Recognition"
        android:textSize="24sp"
        android:textStyle="bold"
        android:layout_marginBottom="16dp"/>

    <!-- ImageView to display the image -->
    <ImageView
        android:id="@+id/imageView"
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:layout_gravity="center"
        android:contentDescription="Image for inference"
        android:layout_marginBottom="16dp"/>

    <!-- Label showing the true label of the image -->
    <TextView
        android:id="@+id/trueLabel"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="True Label: N/A"
        android:textSize="18sp"
        android:layout_marginBottom="16dp"/>

    <!-- Button to select an input image -->
    <Button
        android:id="@+id/selectImageButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Load Image"
        android:layout_marginBottom="16dp"/>

    <!-- Button to run inference -->
    <Button
        android:id="@+id/runInferenceButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Run Inference"
        android:layout_marginBottom="16dp"/>

    <!-- TextView to display the predicted label and inference time -->
    <TextView
        android:id="@+id/predictedLabel"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Predicted Label: N/A"
        android:textSize="18sp"
        android:layout_marginBottom="8dp"/>

    <TextView
        android:id="@+id/inferenceTime"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Inference Time: N/A ms"
        android:textSize="18sp"/>
</LinearLayout>
```

The provided XML code defines a user interface layout for an Android activity using a vertical LinearLayout. It includes several UI components arranged vertically with padding and centered alignment. At the top, there is a TextView acting as a header, displaying the text “Digit Recognition” in bold and with a large font size. Below the header, an ImageView is used to display an image, with a default source set to sample_image. This is followed by another TextView that shows the true label of the displayed image, initially set to “True Label: N/A”.

The layout also contains two buttons: one labeled “Load Image” for selecting an input image, and another labeled “Run Inference” to execute the inference process on the selected image. At the bottom, there are two TextView elements to display the predicted label and the inference time, both initially set to “N/A”. The layout uses margins and appropriate sizes for each element to ensure a clean and organized appearance.

## Add PyTorch to the project
Before going further you will need to add PyTorch do the Android project. To do so, open the build.gradle.kts (Module:app) file and add the following two lines under dependencies:

```XML
implementation("org.pytorch:pytorch_android:1.10.0")
implementation("org.pytorch:pytorch_android_torchvision:1.10.0")
```

The dependencies section should look as follows:
```XML
dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.material)
    implementation(libs.androidx.activity)
    implementation(libs.androidx.constraintlayout)
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)

    implementation("org.pytorch:pytorch_android:1.10.0")
    implementation("org.pytorch:pytorch_android_torchvision:1.10.0")
}
```

## Logic implementation
You will now implement the logic for the application. This will include loading the pre-trained model, loading and displaying images, and running the inference.

Open the MainActivity.kt and modify it as follows:

```Kotlin
package com.arm.armpytorchmnistinference

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import org.pytorch.IValue
import org.pytorch.Module
import org.pytorch.Tensor
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.io.InputStream
import kotlin.random.Random
import kotlin.system.measureNanoTime

class MainActivity : AppCompatActivity() {
    private lateinit var imageView: ImageView
    private lateinit var trueLabel: TextView
    private lateinit var selectImageButton: Button
    private lateinit var runInferenceButton: Button
    private lateinit var predictedLabel: TextView
    private lateinit var inferenceTime: TextView
    private lateinit var model: Module
    private var currentBitmap: Bitmap? = null
    private var currentTrueLabel: Int? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        // Initialize UI elements
        imageView = findViewById(R.id.imageView)
        trueLabel = findViewById(R.id.trueLabel)
        selectImageButton = findViewById(R.id.selectImageButton)
        runInferenceButton = findViewById(R.id.runInferenceButton)
        predictedLabel = findViewById(R.id.predictedLabel)
        inferenceTime = findViewById(R.id.inferenceTime)

        // Load model from assets
        model = Module.load(assetFilePath("model.pth"))

        // Set up button click listener for selecting random image
        selectImageButton.setOnClickListener {
            selectRandomImageFromAssets()
        }

        // Set up button click listener for running inference
        runInferenceButton.setOnClickListener {
            currentBitmap?.let { bitmap ->
                runInference(bitmap)
            }
        }
    }

    private fun selectRandomImageFromAssets() {
        try {
            // Get list of files in the mnist_bitmaps folder
            val assetManager = assets
            val files = assetManager.list("mnist_bitmaps") ?: arrayOf()

            if (files.isEmpty()) {
                trueLabel.text = "No images found in assets/mnist_bitmaps"
                return
            }

            // Select a random file from the list
            val randomFile = files[Random.nextInt(files.size)]
            val inputStream: InputStream = assetManager.open("mnist_bitmaps/$randomFile")
            val bitmap = BitmapFactory.decodeStream(inputStream)

            // Extract the true label from the filename (e.g., 07_00.png -> true label is 7)
            currentTrueLabel = randomFile.split("_")[0].toInt()

            // Display the image and its true label
            imageView.setImageBitmap(bitmap)
            trueLabel.text = "True Label: $currentTrueLabel"

            // Set the current bitmap for inference
            currentBitmap = bitmap
        } catch (e: IOException) {
            e.printStackTrace()
            trueLabel.text = "Error loading image from assets"
        }
    }

    // Method to convert a grayscale bitmap to a float array and create a tensor with shape [1, 1, 28, 28]
    private fun createTensorFromBitmap(bitmap: Bitmap): Tensor {
        // Ensure the bitmap is in the correct format (grayscale) and dimensions [28, 28]
        if (bitmap.width != 28 || bitmap.height != 28) {
            throw IllegalArgumentException("Expected bitmap of size [28, 28], but got [${bitmap.width}, ${bitmap.height}]")
        }

        // Convert the grayscale bitmap to a float array
        val width = bitmap.width
        val height = bitmap.height
        val floatArray = FloatArray(width * height)
        val pixels = IntArray(width * height)
        bitmap.getPixels(pixels, 0, width, 0, 0, width, height)

        for (i in pixels.indices) {
            // Normalize pixel values to [0, 1] range, assuming the grayscale image stores values in the R channel
            floatArray[i] = (pixels[i] and 0xFF) / 255.0f
        }

        // Create a tensor with shape [1, 1, 28, 28] (batch size, channels, height, width)
        return Tensor.fromBlob(floatArray, longArrayOf(1, 1, height.toLong(), width.toLong()))
    }

    private fun runInference(bitmap: Bitmap) {
        // Convert bitmap to a float array and create a tensor with shape [1, 1, 28, 28]
        val inputTensor = createTensorFromBitmap(bitmap)

        // Run inference and measure time
        val inferenceTimeMicros = measureTimeMicros {
            // Forward pass through the model
            val outputTensor = model.forward(IValue.from(inputTensor)).toTensor()
            val scores = outputTensor.dataAsFloatArray

            // Get the index of the class with the highest score
            val maxIndex = scores.indices.maxByOrNull { scores[it] } ?: -1
            predictedLabel.text = "Predicted Label: $maxIndex"
        }

        // Update inference time TextView in microseconds
        inferenceTime.text = "Inference Time: $inferenceTimeMicros µs"
    }

    // Method to measure execution time in microseconds
    private inline fun measureTimeMicros(block: () -> Unit): Long {
        val time = measureNanoTime(block)
        return time / 1000 // Convert nanoseconds to microseconds
    }

    // Helper function to get the file path from assets
    private fun assetFilePath(assetName: String): String {
        val file = File(filesDir, assetName)
        assets.open(assetName).use { inputStream ->
            FileOutputStream(file).use { outputStream ->
                val buffer = ByteArray(4 * 1024)
                var read: Int
                while (inputStream.read(buffer).also { read = it } != -1) {
                    outputStream.write(buffer, 0, read)
                }
                outputStream.flush()
            }
        }
        return file.absolutePath
    }
}
```

## Prepare model and data
