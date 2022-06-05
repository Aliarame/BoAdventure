# Bo: Adventure

**Bo: Adventure** is the very first program and game I've made using Python 3 and Pygame during late 2017 and early 2018 for the final school project "ISN".
The game is a RPG like game similar to Final Fantasy fighting mechanics with a turn-based system.
This game was inspired by an OpenClassroom lesson on Pygame the "DK Labyrinthe" meaning "DK Maze" (the link didn't worked anymore).
I'm making this game open source, this way it will be easier to access and to modify. I wanted to see the differences between my finished project back then, and a current version of this with more stuff added in it and more optimisation.

## Versions

There are currently 4 versions for this project (more information about them below) :
- Legacy Untouched: only to save the original files of the final project. `in FR`
- Legacy Working: if you want the very first experience of the game. `in FR`
- Legacy Enhanced: if you want to play the original game in English and with better images resolution. `in EN`
- Current: if you want to try the game in it's improved version. `in EN`

### Legacy Untouched
The untouched files as they were when I finished the project. Might not work, but it still need to remain unchanged.

### Legacy Working
Almost as the same as Untouched except that it should work on Python3 with Pygame  
The only thing that changed : `event.pos --> pygame.mouse.get_pos()`

### Enhanced
Enhanced is an optimised version of the project without modifying the technical aspect of the game.
It's the middle ground between "Legacy" and "Current".
The major changes are :
- More optimised code
- Better quality images
- More legible dialogs

### Current
This version is the contuinity of the game as if it was always developped with new implementations and optimisations, either for the code or for the technical aspect of the game.

## Installation
Steps for Linux but can work anywhere if you can get python3 and pygame working  
You need to get pip3 python3 and git (here for Debian and Ubuntu based distributions)  
```
sudo apt-get install python3 python3-pip git
```
Then install pygame with pip3
```
pip3 install pygame
```
Now you can clone the game's folder and change to the directory of the version of the game you want to launch
```
git clone https://github.com/AramLF/BoAdventure
cd BoAdventure/enhanced/
python3 enhanced.py
```

## Contributing
Any contributions is welcome if it follows the version goals of the one you're working on.
