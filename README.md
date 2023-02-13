# doom game style using pygame module

<p align="center"><img src="https://assets.stickpng.com/images/580b57fcd9996e24bc43c34d.png" alt="doom" width="25%" border="0"><br /></p>


<h1 align="center"> 🎮 Doom game | Raycaster engine </h1>

## Project Status
<p>:heavy_check_mark: Complete<p>

## Table of Contents 
- [Objective](#objective)
- [Process](#Process)
- [Results](#Results)
- [Authors](#Authors)

## Objective
The goal for this project is to build a doom like game using python alongside with pygame module. Building the raycaster engine as our pseudo 3D model.

## Process
- Initial setup
- Ray casting
- Textures
- Sprites
- Pathfinding Algorithm

## Initial setup
The first step is to setup up a feel parameters that are going to compose our settings file, as well as making our map, which at first, will be a numpy matrix, composed by zeros and ones (zeros being empty space).

## Ray casting
The way that our game will be render is through a ray casting engine, that is, a top-down 2D game with the illusion of a 3D game. I highly recommend watching <a href="https://youtu.be/eOCQfxRQ2pY" target="blank"> Matt Godbolt's </a> video on ray casting as he greatly explains how the engine works.

## Textures
Since our map is composed by a matrix of zeros and ones where ones represent the walls, by assigning different textures to numbers from 1-5 in a dictionary, texturing the walls of the game would be simple. Not that simple that is, as we still need to calculate the offset of the vertical and horizontal interception, which depends of the angle of the player.

## Sprites
By defining two separate classes, one for static and other for animated, we're able to implement sprites into our game. We're also able to re-scale the size of the sprite by multiplying it's projection through a parameter we chose ourselves at the class creation, the same is valid for shifting up and down the sprite image.

## Pathfinding algorithm
To avoid weird movements from the enemies NPC's we implement a pathfinding algorithm called Bread-First-Search (BFS) which is explained in detail by <a href="https://youtu.be/eOCQfxRQ2pY" target="blank"> this video </a> from Coder Space. The same theory is applied to our code, thus making the enemies move in a more intelligent way.

## Results
<p>After all the sprites and NPC's were added the game was playable and with a certain degree of interactivity, having the player surviving the four enemies scattered around the map and the boss in the center.<p>
<p align="center"><img src="resources/gameplay.gif" width = 500 height = 300  alt="gameplay" border="0"><br /></p>

## Challenges
- First time approaching pygame module
- Hard to understand the ray casting at first
- Understand methods and encapsulate them into classes
- Finding the right sprites and reshaping them
- Find suitable audio for the game
## Authors
<p>Jonas Angulski <p>

<p> Source: <a href="https://youtu.be/ECqUrT7IdqQ" target="_blank"> Coder Space </a> absolutely great tutorial for creating a Doom / Wolfstein like game from scratch in python.

<p> Sprites: <a href="https://spritedatabase.net/game/760" target="blank"> https://spritedatabase.net/game/760 </a>

<p> Background Music: <a href="https://www.youtube.com/watch?v=BSsfjHCFosw&ab_channel=JimDarkMagic" target="blank"> https://www.youtube.com/watch?v=BSsfjHCFosw&ab_channel=JimDarkMagic </a> composed by Bobby Prince.











