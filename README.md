# Anaglyph Vision Therapy Game

The Anaglyph Letter Puzzle Game is designed to improve visual and cognitive processing abilities. To play, the user must scan a grid of similar looking sequences to find a hidden target sequence. The goal is to find and select the target(s) as quickly and accurately as possible. A grid is complete when all targets are found, and the game is complete when all grids have been solved. The game offers various levels of difficulty that can be customized based on the user's preference. The player can choose the number of grids to solve, the grid size, the number of targets to find, sequence length, and spacing between rows and columns. Alternatively, the user can choose to play a "Quick Play" game to progress through increasingly difficult grids automatically.

The game is designed to be played while wearing anaglyph lenses, either red/green or red/blue. The user is able to adjust the grid colors so that each eye can only see half the grid. This forces the brain to process information from both eyes, which can lead to reduced suppression. By requiring players to focus on and identify specific sequences while ignoring distractors, the game can help to improve visual effieciency, visual perception, attention, and cognitive flexibility. Therefore, this game can be used as a supplement vision therapy treatment. Gamifying vision therapy exercise by using a challenging letter puzzle game can make treatment more enjoyable and engaging.

This application tracks game parameters, scores, and other metrics. If used for vision therapy treatment, vision therapy providers can register their patients in a database through an online portal. When a petient is loggen in, gameplay data is sent to the database. Pateient performance data is only accessible to the vision therapy providers and can be used to monitor progress.

<img width="600" alt="Screen Shot 2023-05-05 at 9 17 46 PM" src="https://user-images.githubusercontent.com/123909507/236590604-6346a912-3573-4d2a-abe4-8876a7977ae5.png">
<img width="600" alt="Screen Shot 2023-05-05 at 9 19 29 PM" src="https://user-images.githubusercontent.com/123909507/236590780-cc019dd2-b35f-4b65-9e3d-0dc34ec74ea5.png">


# How to Run

To play this game, launch the terminal and clone this repository using the command git clone <link to repository>

Ensure that you have Python installed. Navigate to the application directory. The commands to install the application's dependencies are specific to your device's operating system, so run the commands that correspond with your operating system.

Mac:
```
pip install --upgrade pip
```

Windows:
```
choco install python
python -m pip install --upgrade pip
```


Ubuntu/Debian:
```
sudo apt-get update
sudo apt-get install python3-pip
```


## Project Dependencies

Required Modules are located in `requirements.txt`

If this item is not included or is incomplete, it can be generated via:


```shell
pip install pipreqsnb
pipreqsnb .
```

## Install Dependencies

```
pip3 install protobuf==3.20.1
pip install -r requirements.txt
```
## Launch the Game

From the terminal, run the command:

```
python3 Menu.py
```


# Game Interface:

Menu Page

<img width="600" alt="Screen Shot 2023-05-05 at 2 41 55 AM" src="https://user-images.githubusercontent.com/123909507/236590368-0af5db95-7fb0-40a6-be86-096a46c35f74.png">

Mode Select Page

<img width="600" alt="Screen Shot 2023-05-05 at 6 19 55 PM" src="https://user-images.githubusercontent.com/123909507/236590409-9363033c-ee79-4b28-b965-afbf7ec1e205.png"> 


Settings Page

<img width="600" alt="Screen Shot 2023-05-05 at 6 18 39 PM" src="https://user-images.githubusercontent.com/123909507/236590377-89f7560e-633d-47f0-826d-8093a3a7d8fa.png">


Color Picker Page

<img width="600" alt="Screen Shot 2023-05-05 at 6 46 40 PM" src="https://user-images.githubusercontent.com/123909507/236590939-108e44c1-59aa-42fc-a0ac-8b3fce697a23.png">


Help Page

<img width="600" alt="Screen Shot 2023-05-05 at 6 19 23 PM" src="https://user-images.githubusercontent.com/123909507/236590381-e361d1f7-b66d-43cc-af64-0594cc238194.png">


Login Page

<img width="600" alt="Screen Shot 2023-05-05 at 6 19 32 PM" src="https://user-images.githubusercontent.com/123909507/236590390-20405444-b5d6-43c3-b897-94306b5d68cb.png">


# How to contribute

Follow this project board to know the latest status of the project: [[http://...]([http://...])](https://github.com/orgs/cis3296s23/projects/68)

