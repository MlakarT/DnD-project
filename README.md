# DnD-project

Mapping project for Dungeons and Dragons Tabletop game. This is a dungeon randomizer for my Dungeons and Dragons homebrew campaign: _Kingdoms of Akkamen_. The project is intended to run for the duration of the campaign, and will later be released to the public, but will also be used as part of a school assignment.

Please note that this is the second active repository for this project. The [original repository](https://github.com/MlakarT/DnD-project_archived) has been archived and is out of use, but is still available for viewing.

Also note that some _(most)_ of the code from the original repository has been reused.

## What does it do?

When roleplaying, the Dungeon Master may decide to use a randomly generated dungeon. The Dungeon Master takes a pre-recorded seed to generate a map or chooses one at random. The generator is meant as an extension to a pre-existing dungeon. For example: suppose the group enters an enchanted castle, in which the rooms and corridors are positioned differently every time. The group's goal would then be to make their way through the domain and beat all encounters presented to them by the Dungeon Master.

### How to use the generator

_Random generation_: Click on the "Generate random map" button for a random map. The map will be displayed in the wooden bulletin board in the middle of the window.

_Generating maps from seeds_: After generating your first map, you can choose to display a map from a selected/pre determined seed, by typing it into the **seed box** and pressing the "generate" button below. The map will then be displayed in wooden bulletin board in the middle of the window.

_Loading maps from saves_: When logged in, you can save a map you like, or load a map from your "saves" tab by simply clicking on it. To save a map, click the "save map" button in the bottom right corner of the wooden bulletin board, then head to the saves tab to view your saved maps.

### Importing assets, maps, exporting maps, DnD Beyond

None of this has been added. Please wait until further notice. Thank you.

## Notes about my program and research

I got inspired to do this once while dm'ing, when i suddenly recalled a scene from the game _Genshin impact_, where the player experiences a similar, randomised map in a looping manor.

The app will hopefully be used in at least two sessions of my campaign, once in a chinese-karst-themed domain, and once in a snowy icy mountain maze.

### **What is DnD?**

In Dungeons & Dragons, the players form an adventuring party who explore fantasy worlds together as they embark on epic quests and level up in experience. The Dungeon Master (also known as the DM) is the game's referee and storyteller. There’s no winning or losing in D&D—at least, not in the conventional way.

### **Pseudo number generators and lcg's**

A pseudo random number generator is a type of recursive nmber generator that produces a number based on a set of rules and the previous output.

For this program, a **Linear congruetal generator** (lcg for short) was used. It is a type of recursive, modulus based pseudo number generator, that takes 4 inputs, namely: the modulus, which when dividing by prouces the final number, the multiplier and increment which regulate the recurrence of the numbers, and the seed, the initial  number, which produces the another in a recursive manor.

For the purposes of this program, the Numerical Recipies lcg, which uses a modulus of 2^32, a multiplier of 1664525 and an increment of 1013904223.

For more information about the relevant topics, you can look up [Pseudo RNGs](https://en.wikipedia.org/wiki/Pseudorandom_number_generator), [lcgs](https://en.wikipedia.org/wiki/Linear_congruential_generator) and the [Numerical recipies lcg](https://en.wikipedia.org/wiki/Numerical_Recipes).

### **Assets, animations and art**

Most assets were gotten of off copyright-free websites, the banner and the bulletin board were made by my friend Ajš Vičar, who I thank greatly.

*if the sections above are empty, that's because i'm gonna update them later
*if something mentioned in my README.md isn't in the code yet, that's because I either ran out of time or it is way beyond the scope of the project.
