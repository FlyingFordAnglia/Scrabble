# CLI Scrabble 
#### License: MIT
#### Version 1.0

![screenshot of an active game](https://github.com/Stochastic13/Scrabble/blob/master/screenshot.png)

**CLI SCRABBLE** is a python program to play the game of SCRABBLE in a Command-Line-Interface format.
This program was made as an exercise for fun and some learning, and also is my first GitHub repository! 

## Prerequisites

On top of a working Python 3.5+ installation:
- `numpy`
- `termcolor` (optional, strongly recommended)
- `colorama` (for windows with `termcolor` ; optional, strongly recommended)


## How to Run

Open terminal (in windows: windows button + r -> type `cmd` -> hit enter) -> Navigate to the code folder within the Scrabble repository -> 
Type the following in the terminal to run the game:
```
python inputoutput.py
```

## How to play

Once you run the programme, a CLI dialogue of the game play begins. 
The rules of the game are in accordance with the original Scrabble rules. For more info on the orginal rules, click [here](https://scrabble.hasbro.com/en-us/rules). You can also read the rules line-by-line from within the game too!
The current version of CLI scrabble is a turn based game with no time limit and without a provision for challenging, but a global `validity_mode` controls if only in-the-dictionary words are allowed on the board.
For the default wordlist, we currently use [SOWPODS](https://www.wordgamedictionary.com/sowpods/), but any properly formatted file can be used as the wordlist (details within the game).

## Upcoming Features

1. Provision for challenging with `validity_mode` off
2. Better documentations :)
3. **A graded AI to play against!**
4. Tutor to help you select the best play given a mode
5. A fast python API to allow for training AI (hopefully :) )

## Contributors

[FlyingFordAnglia](https://github.com/FlyingFordAnglia) and [Stochastic13](https://github.com/Stochastic13)
