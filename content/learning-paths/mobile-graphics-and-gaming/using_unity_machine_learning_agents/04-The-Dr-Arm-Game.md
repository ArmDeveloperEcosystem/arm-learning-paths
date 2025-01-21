---
title: The Dr Arm game
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The Dr Arm Game

This learning path is based on the video workshop [Using Unity's Machine Learning Agents on Arm](https://on-demand.arm.com/flow/arm/devhub/sessionCatalog/page/pubSessCatalog/session/1681291098539001B22U) and uses the same Dr Arm game project files (provided in the supporting zip file you extracted earlier).

In the game, you control a fighting character (a Paladin) in battle against an AI opponent (a Vampire).

The battle takes place in a small 3D arena. Both characters can perform the following actions:

* Move (left, right, forward, backward)
* Roll
* Sword attack
* Fireball attack

Use the on-screen touch controls to control your character on mobile. The AI opponent is driven by an AI "brain" created with the ML Agents Toolkit.

## Open and test the game

Before diving into machine learning in Unity, look at the game. There is a ready-to-play version in the Unity scene called _Level_DevSummit2022_ReadyToPlay_.

Later sections of this learning path explain how the model was pre-trained and plugged into the game.

Dr Arm is intended for mobile play but you can test it within the Unity editor first to ensure everything is present and correct. To do this, run the game in demo mode, which shows two AI characters battling each other.

In the default editor layout:

1. Navigate to the _Assets/#DevSummit2022/Scenes_ directory in the Project panel

1. Double-click the scene file _Level\_DevSummit2022\_ReadyToPlay_ (depending on your platform or settings, it may show the _.unity_ file extension)

1. The scene should open inside the _Scene_ tab

1. Click the play button

1. You may some some warnings in the _Console_ tab but these can be ignored as we haven't done all the machine learning steps yet

1. You should be presented with a simple title screen with a menu of _Easy_, _Medium_, _Hard_ and _Demo_ options

![Dr Arm Title Screen](/images/game-title-screen.jpg "Figure 1. Title screen with menu options")

1. Click _Demo_ to run a battle between two AI characters

![Dr Arm Demo Mode](/images/game-demo-mode.jpg "Figure 2. Demo mode running two AT characters against each other")

The screenshots above show a working version. If you see something similar, you know everything is working as expected.

The next section dives into machine learning and how ML is leveraged in Dr Arm.
