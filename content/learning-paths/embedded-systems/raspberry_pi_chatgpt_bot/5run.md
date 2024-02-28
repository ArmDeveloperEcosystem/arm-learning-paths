---
title: Running the Bot
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Running the bot

Activate the virtual environment if you're not still in it
```
source env/bin/activate
```

Then just run main.py
```
python main.py
```

Say "computer", wait a second, then ask your question. Give it a couple seconds and it will audibly reply to you.

It should continue to run indefinitely until you manually stop it

Normal output while it's sitting there waiting to hear the keyword:
![the terminal, waiting for keyword](./terminal1.png)

And waiting for you to speak after hearing the keyword:
![the terminal, listening for you to speak after hearing the keyword](./terminal2.png)

**Note**: The errors you see are normal and do not effect the operation of the bot. I spent some time trying to get rid of them but wasn't able to find a solution, but as everything works as it's supposed to I just let it go
