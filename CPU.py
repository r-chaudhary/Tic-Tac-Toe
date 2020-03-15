# 
# File   : CPU.py
#
# Author : Rahul Chaudhary
# Email  : r.chaudhary@outlook.in
# Date   : 14-March-2020
#
# Summary of File:
#   This file contains the code for Computer as a Player
#   It is the logic of computer player
#

class CPU_play:
    def __init__(self):

        #
        # Weight of every Tile on Board
        # For Example:
        #   Tile [5] on Board comes in the wining combination tile of 4 chains
        #   Such as (1,5,9) (3,5,7) (2,5,8) (4,5,6) so the weight of 5 is 4
        # Here keys are weight and values is the list of tile
        self.weight = {4:[5],3:[1,3,7,9],2:[2,4,6,8]}
        #
        # chain is the win combination of tiles
        # There are 8 wining combinations in Tic Tac Toe
        # 
        self.chain = {1:[1,2,3],2:[4,5,6],3:[7,8,9],4:[1,4,7],5:[2,5,8],6:[3,6,9],7:[1,5,9],8:[3,5,7]}
        self.blockedChain = set()         # Contains chain keys if chain has only opponent values.
        self.reservedChain = set()        # Contains chain keys if chain has only computer value.
        self.freeChain = set()            # Contains chain keys if chain is not blocked and reserved.
        self.commonChain = set()          # Contains chain keys if chain has both values.
        self.board = None
        
    #
    # chainUpdate(self, player)
    # 
    # Updates the values in chain.  
    def chainUpdate(self,player):
        self.reservedChain.clear()
        self.blockedChain.clear()
        self.freeChain.clear()
        for tile,value in self.board.board.items():
            for key,chain in self.chain.items():
                if (value == 'X' and value == player.value) or (value == 'O' and value == player.value):
                    if tile in chain:
                        self.reservedChain.add(key)
                        
                elif (value == 'X' and value != player.value) or (value == 'O' and value != player.value):
                    if tile in chain:
                        self.blockedChain.add(key)

        for i in self.chain.keys():
            if i not in (self.reservedChain.union(self.blockedChain)):
                self.freeChain.add(i)
        for i in self.reservedChain:
            if i in self.blockedChain:
                self.commonChain.add(i)
        for i in self.commonChain:
            self.reservedChain.remove(i)
            self.blockedChain.remove(i)
        for i in self.commonChain:
            check = 0
            for tile,value in self.board.board.items():
                for k in self.chain[i]:
                    if k == tile:
                        if value != str(k):
                            check += 1


    def priorityLevel_1(self):
        if len(self.reservedChain) == 0:
            return 0
        else:
            for i in self.reservedChain:
                chain = self.chain[i]
                value = []
                for j in chain:
                    value.append(self.board.board[j])
                if value[0] == value[1]: return value[2]
                elif value[0] == value[2]: return value[1]
                elif value[1] == value[2]: return value[0]
            return 0

    def priorityLevel_2(self):
        if len(self.blockedChain) == 0:
            return 0
        else:
            for i in self.blockedChain:
                chain = self.chain[i]
                value = []
                for j in chain:
                    value.append(self.board.board[j])
                if value[0] == value[1]: return value[2]
                elif value[0] == value[2]: return value[1]
                elif value[1] == value[2]: return value[0]
            return 0

    def priorityLevel_3(self):
        max_weight = 0
        list = self.freeChain
        if len(list) == 0:
            list = self.commonChain
        if len(list) == 0:
            list = self.reservedChain 
        for i in list:
            for j in self.chain:
                for k,l in self.weight.items():
                    if self.board.board[j] == str(j):
                        if j in l:
                            if max_weight < k:
                                max_weight = k
        for i in self.board.board.values():
            for j in self.weight[max_weight]:
                if i == str(j):                    
                    return j
    

    def play(self,player,board):
        self.board = board
        self.chainUpdate(player)
        level_1 = self.priorityLevel_1()
        if level_1 != 0:
            return level_1
        
        level_2 = self.priorityLevel_2()
        if level_2 != 0:
            return level_2

        level_3 = self.priorityLevel_3()
        if level_3 != 0:
            return level_3
        
        
        
