#!/usr/bin/env python3


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
    
    def display_board(self):
        for i in range(0, 9, 3):
            print(' | '.join(self.board[i:i+3]))
            if (i < 5):
                print('-'*10)
        print("")


    def update_board(self, symbol, index):
        if (self.board[index].isdigit()):
            self.board[index] = symbol
            return True
        return False


    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]
