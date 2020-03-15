# 
# File   : Player.py
#
# Author : Rahul Chaudhary
# Email  : r.chaudhary@outlook.in
# Date   : 15-March-2020
#
# Summary of File:
#   Here the PLayer class 
#   which creates the player object 
#   It stores player name and its value [X or O]
#

import UI

class Player(UI.ScreenConfigure):


    def __init__(self,value,name=None):
        super().__init__()
        # Get Player Name and Value[X/O]
        if name == None:
            print("{}{:<40}".format(' '*(int(self.columns/2)-20), "Player name : "), end="")
            name = input()
        self.name = name
        self.value = value
