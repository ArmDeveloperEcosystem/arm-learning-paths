---
title: One we prepared earlier
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
# Insert training into the game

1. In the Project tab (normally at the bottom left), re-open the original scene by double-clicking it:

`Assets->#DevSummit2022->Scenes->Level_DevSummit2022`

2. Now select the _AgentsSettings_ object, in the _Hierachy_ tab (normally on the left).

![Agent Settings](heirachy-agent-settings.png "Figure 1. Agents Settings")

3. Now in the _Inspector_ (normally on the right) scroll to the _Battle Env Controller (Script)_ and you should see properties for _Easy Battle Brain_, _Normal Battle Brain_ and _Hard Battle Brain_.

3. Next to the _Easy Battle Brain_ there is a cirle. Click it to pop-up the _Select NN Model_ menu, as per Figure 2. 

!["NN Model Pop-up"](battle-enviroment-controller-battle-brain.png "Figure 2. NN Model Pop-up")
Note that you can use the slider in the pop-up to change the list detail view if needed.

4. For each brain there is already a pre-trained version you can use, or if your training has completed use that. Match up each Battle Brain property to an appropriate NN Model.

![Battle Brains](boss-battle-brains.png "Figure 3. Battle Brains")

5. Once the brains are set we can launch the game in the Unity Editor, to make sure everything is working and wired up correctly. If you select "Demo" mode you can see the two ML Agents battle it out.
