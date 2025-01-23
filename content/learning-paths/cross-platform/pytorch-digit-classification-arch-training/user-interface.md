---
# User change
title: "Create an Android Application"

weight: 8

layout: "learningpathall"
---

In this section you will create an Android application to run digit classification. 

The application randomly loads a selected image containing a handwritten digit and its true label. 

The application runs an inference on the image and predicts the digit value. 

## Create an Android project

Start by creating a project:

1. Open Android Studio and create a new project with an **Empty Views Activity**.

2. Configure as follows:
   * Set the project name to **ArmPyTorchMNISTInference**.
   * Set the package name to: **com.arm.armpytorchmnistinference**.
   * Select **Kotlin** as the language.
   * Set the minimum SDK to **API 27 ("Oreo" Android 8.1)**.
   * Set the API to Android 8.1 (API level 27). This version introduced NNAPI, providing a standard interface for running       computationally-intensive machine learning models on Android devices. 

Devices with hardware accelerators can leverage NNAPI to offload ML tasks to specialized hardware, such as Neural Processing Units (NPUs), Digital Signal Processors (DSPs), or Graphics Processing Units (GPUs).

## User interface design

The user interface design contains different components:

- A header.
- `ImageView` and `TextView` sections to display the image and its true label.
- A button to load the image.
- A button to run inference.
- Two `TextView` controls to display the predicted label and the inference time.

Use the editor in Android Studio to replace the contents of `activity_main.xml`, located in `src/main/res/layout` with the following code:

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

The XML code above defines a user interface layout for an Android activity using a vertical `LinearLayout`. It includes several UI components arranged vertically with padding and centered alignment. 

At the top, there is a `TextView` acting as a header, displaying the text **Digit Recognition** in bold and with a large font size. 

Below the header, an `ImageView` displays an image, with a default source set to `sample_image`. 

This is followed by another `TextView` that shows the true label of the displayed image, initially set to `True Label: N/A`.

The layout also contains two buttons: one labeled `Load Image` for selecting an input image, and another labeled `Run Inference` to execute the inference process on the selected image. 

At the bottom, there are two `TextView` elements to display the predicted label and the inference time, both initially set to `N/A`. The layout uses margins and appropriate sizes for each element to ensure a clean and organized appearance.

## Add PyTorch to the project

Add PyTorch to the project by opening the `build.gradle.kts` file and adding the following two lines under dependencies:

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

You will now implement the logic for the application. 

This includes loading the pre-trained model, loading and displaying images, and running inference.

Open `MainActivity.kt` and modify it as follows:

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

This Kotlin code defines an Android app activity called `MainActivity` that performs inference on the MNIST dataset using a pre-trained PyTorch model. The app allows the user to load a random MNIST image from the `assets` folder and run the model to classify the image. 

The `MainActivity` class contains several methods:

* The `onCreate()` method is called when the activity is first created. It sets up the user interface by inflating the layout defined in `activity_main.xml` and initializes several UI components, including an `ImageView` to display the image, `TextView` controls to show the true label and predicted label, and two buttons, `selectImageButton` and `runInferenceButton`, to select an image and run inference. This method then loads the PyTorch model from the `assets` folder using the `assetFilePath()` function, and sets up click listeners for the buttons. The `selectImageButton` is configured to select a random image from the `mnist_bitmaps` folder, while the `runInferenceButton` runs the inference on the selected image.

* The `selectRandomImageFromAssets()` method is responsible for selecting a random image from the `mnist_bitmaps` folder in `assets`. It lists all the files in the folder, picks one at random, and loads it as a bitmap. This method then does the following:
    
    * It extracts the true label from the filename. For example, 07_00.png implies a true label of 7.
    * It displays the selected image in the `ImageView`.
    * It updates the `trueLabel TextView` with the correct label.
    
If there is an error loading the image or the folder is empty, an appropriate error message is displayed in the `trueLabel TextView`.

* The `createTensorFromBitmap()` method converts a grayscale bitmap of size 28x28 (an image from the MNIST dataset) into a PyTorch Tensor, through the following steps:
    
    * The method begins by verifying that the bitmap has the correct dimensions.
    * Then it extracts pixel data from the bitmap.
    * It normalizes each pixel value to a float in the range [0, 1], and stores the values in a float array.
    * Then it constructs and returns a tensor with the shape [1, 1, 28, 28], where 1 is the batch size, 1 is the number of     channels (for grayscale), and 28 represents the width and height of the image. This is required to match the input         expected by the model.

* The `runInference()` method accepts a bitmap as input and performs inference using the pre-trained PyTorch model, through the following steps:

    * First, it converts the bitmap to a tensor using the `createTensorFromBitmap()` method.
    * Then, it measures the time taken to run the forward pass of the model using the `measureTimeMicros()` method.
    * The output tensor from the model, which contains the scores for each digit class, is then processed to determine the     predicted label.
    * The predicted label is displayed in the `predictedLabel TextView`.
    * The method also updates the `inferenceTime TextView` with the time taken for the inference in microseconds.

* The inline function `measureTimeMicros()` is a utility method that measures the execution time of the given code block in microseconds:
   
    * It uses the `measureNanoTime()` function to get the execution time in nanoseconds.
    * It converts the resultant execution time to microseconds by dividing the result by 1000.
    * This method is used to measure the time taken for model inference in the `runInference()` method.

* The `assetFilePath()` method is a helper function that copies a file from the assets folder to the application's internal storage and returns the absolute path of the copied file. This is necessary because PyTorch’s `Module.load()` method requires a file path, not an InputStream. The `assetFilePath()` method does the following:

    * The function reads the specified asset file.
    * It writes its contents to a file in the internal storage.
    * It returns the path to this file.

This method is used in `onCreate()` to load the PyTorch model file, `model.pth`, from the `assets` folder.

* The `MainActivity` class initializes the UI components, loads a pre-trained PyTorch model, and allows the user to select random MNIST images and run inference on them.

Each method is designed to handle a specific aspect of the functionality, such as loading images, converting them to tensors, running inference, and measuring execution time. The code is modular and organized, making it easy to understand and maintain.

To be able to successfully run the application, you need to add the model and prepare the bitmaps. Continue with this Learning Path to learn how to prepare the data.
