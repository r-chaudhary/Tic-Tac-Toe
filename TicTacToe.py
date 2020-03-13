# 
# File   : TicTacToe.py
#
# Author : Rahul Chaudhary
# Email  : r.chaudhary@outlook.in
# Date   : 14-March-2020
#
# Summary of File:
#   This file contains the code of Tic Tac Toe Game.
#   It contains the Main Menu of the game.
#

 
from Player import Player
import UI
from Game import Game
import os

EXIT = False


class TicTacToe(UI.ScreenConfigure):
    def __init__(self):
        super().__init__()
        
        self.MainMenu()

    #
    # playWithCPU(self)
    # 
    # Summary of playWithCPU method:
    #   The playWithCPU, extends the feature of Tic Tac Toe game
    #   to play with a human and CPU 
    def playWithCPU(self):

        # Get Human Value [X/O]
        print("{}{:<40}".format(' '*(int(self.columns/2)-20), "Select X / O > "), end="")
        sel = input()

        # Initialize Players
        if sel == 'X':
            Player1 = Player('X')
            Player2 = Player('O','COMPUTER')
        else:
            Player1 = Player('X','COMPUTER')
            Player2 = Player('O')

        # Initialize Board    
        Board = UI.UI()

        # Initialize Game
        G = Game(Player1,Player2,Board,mode='C')  

        # Start Playing!  
        G.play()


    def playWithHuman(self):

        # Initialize Player
        Player1 = Player('X')
        Player2 = Player('O')

        # Initialize Board
        Board = UI.UI()

        # Initialize Game
        G = Game(Player1,Player2,Board,mode='H')

        # Start Playing!
        G.play()

    def exit(self):
        global EXIT

        # SET EXIT to True 
        EXIT = True
    
    # Main Menu
    def MainMenu(self):
        
        # Clear Terminal
        os.system(self.clrcmd)

        # Skip n lines to make everything appear in center
        print("\n"*(int(self.rows/2)-7))

        # Print Menu Command Text
        print("{}{:^40}".format(' '*(int(self.columns/2)-20), "Welcome to Tic Tac Toe"))
        print("{}{:<40}".format(' '*(int(self.columns/2)-20), "1] Play with CPU"))
        print("{}{:<40}".format(' '*(int(self.columns/2)-20), "2] Play with Human"))
        print("{}{:<40}".format(' '*(int(self.columns/2)-20), "3]Exit"))
        print("{}{:<40}".format(' '*(int(self.columns/2)-20), self.prompt), end="")

        # Get user input
        opt = int(input())

        if   opt == 1 : self.playWithCPU()
        elif opt == 2 : self.playWithHuman()
        elif opt == 3 : self.exit()

# Start Tic Tac Toe Game
while EXIT is False:
    T = TicTacToe()
