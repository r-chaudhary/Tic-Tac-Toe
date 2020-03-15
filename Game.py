# 
# File   : Game.py
#
# Author : Rahul Chaudhary
# Email  : r.chaudhary@outlook.in
# Date   : 14-March-2020
#
# Summary of File:
#   This file contains all the logics of the game.
#   It contains Game class 
#

from CPU import CPU_play
import UI

#
# class Game
#
# This class have functionality of the game. It starts,
# sechdule player, checks for winner, checks if duplicate 
# tile is pressed. 

class Game(UI.ScreenConfigure):
    def __init__(self,Player1,Player2,Board,mode):
        super().__init__()
        self.player1 = Player1
        self.player2 = Player2
        self.board = Board
        self.mode = mode
        self.covered_tile = []
        self.current_player = None
        self.movehistory = []


    # It return the number of total element in the board
    #   For example:
    #   Board --> {['X',2,3]
    #              [4,5,'O']
    #              ['X','O',9]
    #              }
    #   Then checkBoard will return 7
    #   as checkBoard only consider the elements only once.
    def checkBoard(self):
        boardItem = self.board.board.values()
        return len(set(boardItem))


    # It is a method used to check is the tile is valid for placing an element or not
    # It return the a message if X or O is already present on the tile
    # If the tile is valid then it will replace the element on the tile to [X or O]
    def checkValidTile(self,data,player):
        data = str(data)
        if data.isdigit() is False:
            print("{}{:<40}".format(' '*(int(self.columns/2)-20), "Invalid section of tile"))
            return self.get(self.current_player)
        elif data not in self.covered_tile:
            self.covered_tile.append(data)
            self.board.board[int(data)] = player.value
            self.movehistory.append([player.name,data])
        else:
            print("{}{:<40}".format(' '*(int(self.columns/2)-20), "Invalid section of tile"))
            print("{}{:<40}".format(' '*(int(self.columns/2)-20), "Element Present"))
            return self.get(self.current_player) 
        
    # This function is used for taking the the input from the user and validating it
    def get(self,player,player_type = None):
        print("{}+{:<40}+".format(' '*(int(self.columns/2)-20), "-"*40))
        
        if player_type != None:
            inp = player_type.play(player,self.board)
            print("{}|{:<40}|".format(' '*(int(self.columns/2)-20), player.name+" [tile no] -> "+str(inp)))
        else:
            print("{}  {:<20}".format(' '*(int(self.columns/2)-20), player.name+" [tile no] -> "), end='')
            inp = input()
        print("{}+{:<40}+".format(' '*(int(self.columns/2)-20), "-"*40))
        self.checkValidTile(inp,player)


    # This function is used for changing the player after a player enter it data
    def checkPlayer(self):
        if self.current_player == None:
            self.current_player = self.player1
        elif self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

            
    # This function check the winner of the game 
    def checkWinner(self):
        boardItem = list(self.board.board.values())
        win_comb = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for i in win_comb:
            s = [boardItem[j-1] for j in i]
            if s == ['X','X','X'] or s == ['O','O','O']:
                self.board.displayBoard(self.movehistory)
                print("{}+{:<40}+".format(' '*(int(self.columns/2)-20), "-"*40))
                print("{}|{:^40}|".format(' '*(int(self.columns/2)-20), "Winner : "+self.current_player.name ))
                print("{}+{:<40}+".format(' '*(int(self.columns/2)-20), "-"*40))
                print()
                print("{}{:^40}".format(' '*(int(self.columns/2)-20), "Enter to Main Menu" ))
                input()
                return 2
        return self.checkBoard()
                            
    #
    # play(self)
    #
    # It starts the game

    def play(self):
        
        check = self.checkBoard()
        # Initilize Computer Player
        if self.mode == 'C':
            computer = CPU_play()

        # Run until Board is filled
        while check != 2:
            self.board.displayBoard(self.movehistory)
            self.checkPlayer()

            if self.current_player.name == 'COMPUTER':
                self.get(self.current_player,computer)
            else:
                self.get(self.current_player)
            check = self.checkWinner()
        if  self.checkBoard() == 2:
                self.board.displayBoard(self.movehistory)
                print("{}+{:<40}+".format(' '*(int(self.columns/2)-20), "-"*40))
                print("{}|{:^40}|".format(' '*(int(self.columns/2)-20), "Match Draw"))
                print("{}+{:<40}+".format(' '*(int(self.columns/2)-20), "-"*40))
                print()
                print("{}{:^40}".format(' '*(int(self.columns/2)-20), "Enter to Main Menu" ))
                input()
                