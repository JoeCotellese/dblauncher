# DOSBox Game Launcher

This is a command-line tool for managing and launching DOSBox games. It allows you to create game directories, delete them, launch games, and install games from .zip files.

## Requirements

Python 3.6 or higher
pipenv

## Installation
First, clone the repository:

    git clone https://github.com/yourusername/dosbox-game-launcher.git
    cd dosbox-game-launcher

Next, set up your Python environment using pipenv:


    pip install pipenv  # If you don't have pipenv installed yet.
    pipenv install

This will create a virtual environment and install all necessary dependencies.

## Usage
To use the DOSBox Game Launcher, first activate your pipenv shell:

    pipenv shell

You can use the following options

To create a new game directory (if it doesn't exist) or launch an existing game:

python dblauncher.py GAMENAME

To delete a game directory:

    python dblauncher.py GAMENAME --delete

To install a game from a .zip file (this will also create the game directory if it doesn't exist):


    python dblauncher.py GAMENAME --install PATH_TO_ZIP_FILE.zip 

Replace GAMENAME with the name of your game and PATH_TO_ZIP_FILE.zip with the path to your .zip file.

Please note that all games are stored in /Volumes/External/DOSBox. You can change this by modifying the games_directory variable in dblauncher.py.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT