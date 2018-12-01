# MIT 6.804 Final Project - Modeling Human Intuition for Object Collision
---------------------

This repository includes the simple simulation model used to infer human inuition for object collision as well as the game engine developed via pygame. 

**Simulation** is the major game engine - contains all levels and game environment. 

**Inference** is the file for inferring model result. No changes should be made here. 


Project Setup
---------------
## Installation

This project was built and tested on MacOS Mojave. I recommend using Python >= 3.6.1 as your default system-wide Python environment

### Python Package Dependencies

	$ pip3 install matplotlib 
	$ pip3 install pandas 
	$ pip3 install numpy
	$ pip3 install scipy 
	$ python3 -m pip install -U pygame --user


## Running the Game 

0. Start simulator (run in terminal) 
```
python3 simulator.py 
```
1. Enter username (If you are a MIT student, please just use your kerberos) 

2. Play game 

## Game Instructions 

There are a total of 11 levels, with the first one being the tutorial level so you can get familiar with the setup. The goal of the game is to predict the block (red or green) in which you believe the moving ball will hit first. Every level ends with the ball hitting one of the two blocks. 

Upon start of a level, you will press either 'Start' or 'Next' to proceed. If you feel confident about the ball hitting one of the two blocks, please **click and hold on** to the button. If you change your mind throughout that level, you can always feel free to click the other button. If you are simply unsure, especially at the beginning of a level, you can choose not to click on any button. 

Your results will be recorded in the rawData directory with your entered username + level. It will be used as an input to compare with the model outcome. 
