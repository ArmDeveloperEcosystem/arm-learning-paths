---
title: Fine-Tune DistilBERT
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Fine-Tune the Model

Using a file editor of your choice, create a file named distilbert-sentiment-analysis.py with the code shown below:

```python
from transformers import DistilBERTTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load dataset and tokenizer
dataset = load_dataset("imdb")
tokenizer = DistilBERTTokenizerFast.from_pretrained("distilbert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

# Tokenize data
dataset = dataset.map(tokenize, batched=True)

# Load pretrained model
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"].shuffle().select(range(2000)),
    eval_dataset=dataset["test"].shuffle().select(range(500))
)

trainer.train()

# Save model
model.save_pretrained("distilbert_sentiment")
```

#TODO: Talk about what the example does.


Run the model using:
```bash
python distilbert-sentiment-analysis.py
```

The output should look like:
```bash
#TODO add output
```
You are now ready to optimize and convert the model using ExecuTorch.


## Compile and build the executable

Start by setting some environment variables that are used by ExecuTorch.

```bash
export ET_HOME=$HOME/executorch
export executorch_DIR=$ET_HOME/build
```

Then, generate a `.pte` file using the Arm examples. The Ahead-of-Time (AoT) Arm compiler will enable optimizations for devices like the Raspberry Pi and the Corstone-320 FVP. Run it from the ExecuTorch root directory.

Navigate to the root directory using:

```bash
cd ../../../
```
You are now in $HOME/executorch and ready to create the model file for ExecuTorch.


```bash
cd $ET_HOME
python -m examples.arm.aot_arm_compiler --model_name=examples/arm/distilbert-sentiment-analysis.py \
--delegate --quantize --target=ethos-u85-256 \
--so_library=cmake-out-aot-lib/kernels/quantized/libquantized_ops_aot_lib.so \
--system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only
```

From the Arm Examples directory, you build an embedded Arm runner with the `.pte` included. This allows you to get the most performance out of your model, and ensures compatibility with the CPU kernels on the FVP. Finally, generate the executable `arm_executor_runner`.

```bash
cd $HOME/executorch/examples/arm/executor_runner


cmake -DCMAKE_BUILD_TYPE=Release \
-DCMAKE_TOOLCHAIN_FILE=$ET_HOME/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
-DTARGET_CPU=cortex-m85 \
-DET_DIR_PATH:PATH=$ET_HOME/ \
-DET_BUILD_DIR_PATH:PATH=$ET_HOME/cmake-out \
-DET_PTE_FILE_PATH:PATH=$ET_HOME/simple_nn_arm_delegate_ethos-u85-256.pte \
-DETHOS_SDK_PATH:PATH=$ET_HOME/examples/arm/ethos-u-scratch/ethos-u \
-DETHOSU_TARGET_NPU_CONFIG=ethos-u85-256 \
-DPYTHON_EXECUTABLE=$HOME/executorch-venv/bin/python3 \
-DSYSTEM_CONFIG=Ethos_U85_SYS_DRAM_Mid  \
-B $ET_HOME/examples/arm/executor_runner/cmake-out

cmake --build $ET_HOME/examples/arm/executor_runner/cmake-out --parallel -- arm_executor_runner

```

Now, you can run the model on the Corstone-320 FVP.