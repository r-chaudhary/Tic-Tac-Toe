# Tic Tac Toe
# Developer : Rahul Chaudhary
# Contact : r.chaudhary@outlook.in

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
