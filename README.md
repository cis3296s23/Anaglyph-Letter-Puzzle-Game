# Anaglyph Vision Therapy Game

This computer application is designed to make vision therapy exercises more enjoyable by gamifying them into a challenging letter puzzle game. To play, users must scan a grid of similar looking sequences to find a hidden target character or symbol. The game's difficulty levels and features can be customized by the user. They can also choose to play a quick version that increases in difficulty as their performance improves. To train their eye teaming skills, users can opt to wear red-blue anaglyph lenses that limit each eye's ability to see half of the items in the grid. The application tracks game parameters, scores, and other metrics to record and monitor user performance, which will be held in a database only accessible to the vision therapy providers.  
  
<img width="686" alt="Screen Shot 2023-04-03 at 5 55 13 AM" src="https://user-images.githubusercontent.com/123909507/229476595-070cdf54-3ca2-468e-a8db-2b42ad4ebb93.png">

# How to run
To play this game, launch their terminal, clone the above repository, and ensure that you have Python and the program’s dependencies installed. Navigate to the directory where the application file is saved in the terminal/command prompt before running the command. The commands to do the above are OS specific. They are labeled by OS: 

Mac: 
pip install --upgrade pip 
pip install pygame 
pip install pygame_gui

Windows: 
choco install python 
python -m pip install --upgrade pip 
pip install pygame 
pip install pygame_gui

Ubuntu/Debian: 
sudo apt-get update
sudo apt-get install python3-pip 
sudo apt-get install python3-pygame
pip install pygame_gui

CentOS:
sudo yum install python3 
sudo yum install python3-pip
sudo yum install python3-pygame
pip install pygame_gui

To run the program: python3 proof_of_concept.py

## Project Dependencies

Required Modules are located in `requirements.txt`

If this item is not included it can be generated via:

```shell
pip install pipreqsnb
pipreqsnb .
```
## Install Dependencies

```
pip install -r requirements.txt
```

# How to contribute
Follow this project board to know the latest status of the project: [http://...]([http://...])  

### How to build
- Use this github repository: ... 
- Specify what branch to use for a more stable release or for cutting edge development.  
- Use InteliJ 11
- Specify additional library to download if needed 
- What file and target to compile and run. 
- What is expected to happen when the app start. 
