# Tic Tac Toe
# Developer : Rahul Chaudhary
# Contact : r.chaudhary@outlook.in

import shutil
import os
import platform

class ScreenConfigure:
    def __init__(self):
        # Define prompt
        self.prompt = '> '

        # Get Terminal Size
        self.columns, self.rows = shutil.get_terminal_size()

        # Get OS Type
        ostype = platform.uname()[0]
        if ostype == "Linux":
            self.clrscr = "clear"
        elif ostype == "Windows":
            self.clrscr = "cls"

        # Check Required Columns
        if self.rows < 15:
            os.system(self.clrcmd)
            print("Enter in Full Screen Mode and Continue...")
            input("Enter to Referesh")
            return
    
    def CLRCSR(self):
         # Clear Terminal
        os.system(self.clrscr)

        # Skip n lines to make everything appear in center
        print("\n"*(int(self.rows/2)-7))

class UI(ScreenConfigure):
    def __init__(self):
        super().__init__()
        self.board = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

    def displayBoard(self, lastmoves):
        self.CLRCSR()

        row_1 = self.board[1]+' | ' + self.board[2]+' | ' +self.board[3]
        row_2 = self.board[4]+' | ' + self.board[5]+' | ' +self.board[6]
        row_3 = self.board[7]+' | ' + self.board[8]+' | ' +self.board[9]

        if len(lastmoves) == 0:
            for i in range(4):
                lastmoves.append(['','']) 
        elif len(lastmoves) < 4: 
            max = len(lastmoves) - 1
            for i in range(4-max,5):
                lastmoves.append(['',''])

        total = 0
        for i in lastmoves:
            if i[1] != '':
                total += 1

        print("{}{:^40}{}|{}".format(' '*(int(self.columns/2)-20), row_1, "Last 4 Moves "," Total Moves :"+str(total)))
        print("{}{:^40}{:<20}{:^5}".format(' '*(int(self.columns/2)-20), '-'*9, lastmoves[-4][0],' -> '+str(lastmoves[-4][1])))
        print("{}{:^40}{:<20}{:^5}".format(' '*(int(self.columns/2)-20), row_2, lastmoves[-3][0],' -> '+str(lastmoves[-3][1])))
        print("{}{:^40}{:<20}{:^5}".format(' '*(int(self.columns/2)-20), '-'*9, lastmoves[-2][0],' -> '+str(lastmoves[-2][1])))
        print("{}{:^40}{:<20}{:^5}".format(' '*(int(self.columns/2)-20), row_3, lastmoves[-1][0],' -> '+str(lastmoves[-1][1])))
        print()
