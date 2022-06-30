import sys
import time

import pyfiglet
from clint.textui import colored


def welcome():
    welcome_caption = pyfiglet.figlet_format("WELCOME IN BATTLESHIP !", font="slant")
    print(colored.red(welcome_caption))
    time.sleep(1)


def about(): 
    welcome_caption = pyfiglet,figlet_format("ABOUT BATTLESHIP", font="slant") 
    print(colored.red(welcome_caption))
    print("""Battleship (also known as Battleships or Sea Battle) is a strategy type guessing game for two players. 
    It is played on ruled grids (paper or board) on which each player's fleet of warships are marked.
     The locations of the fleets are concealed from the other player. 
     Players alternate turns calling "shots" at the other player's ships, 
     and the objective of the game is to destroy the opposing player's fleet.
        """)
    confirm = input("press any key to continue")
    get_game_mode()


def display_instructions():
    pass


def exit_game():
    raise SystemExit


def get_game_mode():
    """
        Should print a menu with the following options:
        1. Human vs Human
        2. Human vs AI
        3. AI vs AI

        The function should return a number between 1-3.
        If the user will enter invalid data (for example 5), than a message will appear
        asking to input a new value.
        The function prints the instructions of a game if option 4 is chosen. Then calls itself and asks user to choose
        game mode unless user chooses to end the game typing quit, exit or close.
        """

    print("""
    Game modes:
        1. Human vs Human
        2. Human vs AI
        3. AI vs AI
    Instructions:
        4. Display legend
        5. About battleship
            """)
    while True:
        player_input = input("Choose a game mode typing an option from one to three: ")
        if player_input == "quit" or player_input == "exit" or player_input == "close":
            print("Bye bye!")
            exit_game()
        else:
            try:
                game_mode = int(player_input)
            except ValueError:
                print("Please enter a number! Choose from 1-4: ")
                continue
            if game_mode < 1 or game_mode > 5:
                print("Wrong choice. Please choose option between 1-4")
                continue
            if game_mode == 4:
                display_instructions()
                get_game_mode()
            if game_mode == 5:
                about()



            else:
                return game_mode


def goodbye():
    goodbye_caption = pyfiglet.figlet_format("GOODBYE !", font="slant")
    print(colored.red(goodbye_caption))
    exit_game()


def get_player_names(game_mode):
    players = []
    if game_mode == 1:
        players.append(input("First player, enter your name: "))
        players.append(input("Second player, enter your name: "))
    return players

