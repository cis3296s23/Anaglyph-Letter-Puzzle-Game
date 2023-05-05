# Anaglyph Vision Therapy Game

The Anaglyph Letter Puzzle Game is designed to improve visual and cognitive processing abilities. To play, the user must scan a grid of similar looking sequences to find a hidden target sequence. The goal is to find and select the target(s) as quickly and accurately as possible. A grid is complete when all targets are found, and the game is complete when all grids have been solved. The game offers various levels of difficulty that can be customized based on the user's preference. The player can choose the number of grids to solve, the grid size, the number of targets to find, sequence length, and spacing between rows and columns. Alternatively, the user can choose to play a "Quick Play" game to progress through increasingly difficult grids automatically.

The game is designed to be played while wearing anaglyph lenses, either red/green or red/blue. The user is able to adjust the grid colors so that each eye can only see half the grid. This forces the brain to process information from both eyes, which can lead to reduced suppression. By requiring players to focus on and identify specific sequences while ignoring distractors, the game can help to improve visual effieciency, visual perception, attention, and cognitive flexibility. Therefore, this game can be used as a supplement vision therapy treatment. Gamifying vision therapy exercise by using a challenging letter puzzle game can make treatment more enjoyable and engaging.

This application tracks game parameters, scores, and other metrics. If used for vision therapy treatment, vision therapy providers can register their patients in a database through an online portal. When a petient is loggen in, gameplay data is sent to the database. Pateient performance data is only accessible to the vision therapy providers and can be used to monitor progress.


<img width="686" alt="Screen Shot 2023-04-03 at 5 55 13 AM" src="https://user-images.githubusercontent.com/123909507/229476595-070cdf54-3ca2-468e-a8db-2b42ad4ebb93.png">

#How to Run

To play this game, launch the terminal and clone this repository using the command git clone <link to repository>

Ensure that you have Python installed. Navigate to the application directory. The commands to install the application's dependencies are specific to your device's operating system, so run the commands that correspond with your operating system.

Mac:
pip install --upgrade pip

Windows:
choco install python
python -m pip install --upgrade pip


Ubuntu/Debian:
sudo apt-get update
sudo apt-get install python3-pip


## Project Dependencies

Required Modules are located in `requirements.txt`

If this item is not included it can be generated via:


```shell
pip install pipreqsnb
pipreqsnb .
```

## Install Dependencies

```
pip3 install protobuf==3.20.1
pip install -r requirements.txt
```
#Launch the Game

From the terminal, run the command:
python3 Menu.py


# How to contribute

Follow this project board to know the latest status of the project: [http://...]([http://...])

### How to build

-   Use this github repository: ...
-   Specify what branch to use for a more stable release or for cutting edge development.
-   Use InteliJ 11
-   Specify additional library to download if needed
-   What file and target to compile and run.
-   What is expected to happen when the app start.
