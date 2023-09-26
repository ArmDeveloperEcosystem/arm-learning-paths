---
title: Setup
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Configuring the NPC _Ray Perception Sensor 3D_ component
1. Select _ML-NPC_ by going to the _Level-DevSummit2022->AgentS Settings->ML-NPC_, as per Figure 1.

![ML-NPC](agent-settings-ml-npc.png "Figure 1. ML-NPC")

2. Next in the Property Inspector on the right click the _Add Component_ button, at the bottom, as per Figure 2. Notice that there are 2 warning in the property inspector.

![Add Component](inspector-add-component.png "Figure 2. Add Component")

3. Now type _ray_ in the filter edit box, to narrow down the search and from the filtered list double click on _Ray Perception Sensor 3D_ to add this componeent to the ML-NPC object.

![Ray Perception Sensor 3D](ray-perception-component.png "Figure 3. Ray Perception Sensor 3D")

4. Notice that by adding the _Ray Perception Sensor 3D_ component, the _Model contains...._ warning message has now disappeared.

5. Now we need to change some properties to complete this component's set-up
* Set the _Sensor Name_ property to "NPCRayPerceptionSensor"
* Add 2 _Detectable Tags_ elements and name them
    * "Player"
    * "Collide"
* Set _Rays Per Direction_ to "20"
* Set _Max Ray Degrees_ to "180"
* Set _Ray Length_ to "30"
* Set _Stacked Ray Traces_ to "3" (Notice how the _An Obsveation of the model..._ warning message has now disappeared)
* Set _Start Vertical Offset_ to "1"
* Set _End Vertical Offset_ to "1"
* The fully working component, with the correct properties updated, should look like this:
![Working Ray Perception Sensor 3D](working-ray-perception-sensor.png "Figure 4. Working Ray Perception Sensor 3D")


## Script Modifications
### Agent Dr Arm

1. With the ML-NPC still selected, in the Inspector, on the right, scroll until you see the _Agent Dr Arm (Script)_. To the right are 3 vertical elipses. Click it to pop-up the context menu and select the _Edit Script_ menu, at the bottom.
![Agent Dr Arm menu](agent-dr-arm-menu.png "Figure 5. Agent Dr Arm menu")

This should launch Visual Studio with the _AgentDrArm.cs_ file ready to be edited.
![Agent Dr Arm Script](agent-dr-arm-cs-script.png "Figure 6. Agent Dr Arm Script")

2. Scroll down to the _CollectObservations()_ method. This method is key so that the reinforcment learning can make good decisions. 

3. Look for _// WORKSHOP TODO:_ and uncomment the lines of code for the player, and a bit further down for the NPC

4. Now scroll down to the _OnActionRecieved()_ method. The other side of re-inforcement learning is knowing the state but alos getting a reward. So knowing whether out actions where successful or not, so our NPC can learn to do the right thing.

5. So again look for _// WORKSHOP TODO:_ in this method and uncomment the line below it, which uses the _m_Existential_ value we calculated earier, to reward the NPC, every 5 frames.


### Battle Environment Controller
1. Now select the _Agent Settings_ object, in the _Heirachy_ tab, on the left.
![Agent Settings](heirachy-agent-settings.png "Figure 7. Agent Settings")

2. Then on the rigt side, in the Inspector, scroll until you see the _Battle Environment Controller (Script)_. To the right are 3 vertical elipses. Click it to pop-up the context menu and select the _Edit Script_ menu, at the bottom.
![Battle Environment Controller menu](battle-enviroment-controller-script.png "Figure 8. Battle Environment Controller menu")

This should launch Visual Studio with the _BattleEnvController.cs_ file ready to be viewed.
![Battle Environment Controller Script](battle-env-controller-cs-script.png "Figure 9. Battle Environment Controller Script")

### Battle Environment Controller Script Walkthrough
Here we'll talk about what various parts of this script does:

Go to Line _47_, where you'll see we have a _BattleMode_ enumeration class to keep track of the difficulty level we are fighting, so that we can determine which "brain" we want to use to, to make our decisions. We're switching brains
depending on how hard it is.

Go to line _118_, to the _FixedUpdate()_ method and here we are largely checking for end
conditions and si the battle over. So mainly if someone has died, as that's a good
indicator that the battle's over, and then we give the appropriate win or loss
depending on who one died. We activate those give and give the
reward the right way, around line _150_.  

If we're training the model (line _165_), then we we put out a nice message as well just so that we can keep track of what is going on.

Also if we're doing training (line _187_), we check if it's taking too long. You can take ages in the real battle, but during training we don't want them both just standing around forever. So after a certain amount of time we decide that they both lose. No winners or losers. We just start again and give them another chance to do better. 

Then regardless if if we've lost, we reset the scene, ready for the
next set of training.

Go to line _244_, to the _ResetScene()_ method and here, when training (line _254_), we put the start position just slightly off because we don't always start from exactly the same place, we don't want to learn to attack from a particular or specific position. We want to learn to attack the enemy from anywhere, so to stop any weird kind of start conditions, or anything like that, we shuffle the player or the player and the enemy a little bit so they start from slightly different places, to avoid that.

Go to line _106_, to the _Update()_ method, so on the update this is being called each frame but all very rarely happen or just really just kind of start, stop and pause that we're detecting here. If a mode changes (line _108_) then we need to configure the agent and put the correct brain in. So either generally at the start of the battle or at the end of the battle.

Go to line _213_, to the _configureAgent()_ method, we enable the battle (line _215_) if we're not paused. We then check if it's the player and we're not in demo mode or training mode, then we take the brain out, we set the brain to null (line _219_), because the player is providing the action not the neural network. 

Otherwise we set the brain appropriately (from line 223__). So if we're in Easy Mode, we get the easy brain. If we're in hard mode we have the hard brain part and then demo mode we've got the normal brain, which could be anything and when we pause we take the brain out, just to make sure that nothing odd is going on.

Then around line _277_ these are all the start conditions starting that get called from the game's menu, whether you're starting a demo or the easy mode or the hard mode. 