"""
dblauncher - a dosbox configuration and launching utility
dblauncher makes it easy to configure dosbox games as well as launch and play them
dblauncher is invoked as follows:

dblauncher GAMENAME

if GAMENAME exists, launch dosbox using the name of the game
of GAMENAME doesn't exist, create a dosbox folder to house the game. Include DOSBox configuration in that folder.

"""
import os
import shutil
import subprocess
import zipfile

import click

games_directory = "/Volumes/External/DOSBox"


def create_game_directory(game_path):
    # If the game doesn't exist, create a new directory for it.
    os.makedirs(game_path)
    os.makedirs(os.path.join(game_path, 'C.disk'))
    # Create a default DOSBox configuration file.
    with open(os.path.join(game_path, 'dosbox.conf'), 'w') as f:
        f.write('[autoexec]\n')
        f.write('# Lines in this section will be run at startup.\n')
        f.write(f'mount C {game_path}/C.disk\n')  # Add this line to mount the C.disk directory.
        f.write('C:\n')
    click.echo(f'Created new game directory and configuration at {game_path}')


def launch_game(game_path):
    # If the game exists, launch DOSBox with the game's configuration.
    subprocess.run(['dosbox', '-conf', os.path.join(game_path, 'dosbox.conf')])


def delete_game_directory(game_path):
    # If the --delete option is provided, ask for confirmation then delete the folder.
    if click.confirm(f'Are you sure you want to delete {game_path}?'):
        shutil.rmtree(game_path)
        click.echo(f'Deleted {game_path}')

def install_game(zip_file, game_path):
    # Unzip the contents into the C.disk folder.
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(game_path, 'C.disk'))

@click.command()
@click.argument('gamename')
@click.option('--delete', is_flag=True, help='Delete the game folder.')
@click.option('--install', type=click.Path(exists=True), help='Install a game from a .zip file.')
def dblauncher(gamename, delete, install):
    game_path = os.path.join(games_directory, gamename)

    if delete:
        delete_game_directory(game_path)
    elif install:
        if not os.path.exists(game_path):
            create_game_directory(game_path)
        install_game(install, game_path)
    elif not os.path.exists(game_path):
        create_game_directory(game_path)
    else:
        launch_game(game_path)


if __name__ == '__main__':
    dblauncher()
