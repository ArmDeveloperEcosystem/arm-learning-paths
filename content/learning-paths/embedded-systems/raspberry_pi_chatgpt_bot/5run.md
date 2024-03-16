---
title: Run and test the bot
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You should still be in the Python virtual environment, but if you are not or if you open a new terminal, make sure to activity the virtual environment using: 

```console
cd $HOME/assistant
source env/bin/activate
```

Run the application:

```console
python main.py
```

Say the wake work, "computer", wait a second, then ask a question. 

Wait a couple seconds and it will audibly reply to you.

The application will run indefinitely until you manually stop it (use Ctrl+C). 

The normal output while the application is waiting for the keyword is shown below: 

![the terminal, waiting for keyword](./terminal1.png)

After the keyword is heard, you will see the `Please speak...` message indicating it is ready for your question: 

![the terminal, listening for you to speak after hearing the keyword](./terminal2.png)

{{% notice Note %}}
The errors are normal and do not effect the operation of the bot. 
{{% /notice %}}

You have constructed a bot on your Raspberry Pi which wakes up on a keyword and answers your questions. 
