import numpy as np

class sudok_square:
    def __init__ (self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
    def add(self):
        tot = np.sum(self.row1 + self.row2 + self.row3)
        return True if tot == 45 else False

def valid_solution(board):
    b = np.sum(board, axis = 1)
    print(b)
    print(min(b))
    if min(b) != 45: return False
    a = np.sum(board, axis = 0)
    if min(a) != 45: return False
    sqr1 = sudok_square(board[0][:3],board[1][:3],board[2][:3])
    sqr2 = sudok_square(board[0][3:6],board[1][3:6],board[2][3:6])
    sqr3 = sudok_square(board[0][6:],board[1][6:],board[2][6:])
    sqr4 = sudok_square(board[3][:3],board[4][:3],board[5][:3])
    sqr5 = sudok_square(board[3][3:6],board[4][3:6],board[5][3:6])
    sqr6 = sudok_square(board[3][6:],board[4][6:],board[5][6:])
    sqr7 = sudok_square(board[6][:3],board[7][:3],board[8][:3])
    sqr8 = sudok_square(board[6][3:6],board[7][3:6],board[8][3:6])
    sqr9 = sudok_square(board[6][6:],board[7][6:],board[8][6:])
    
    if sqr1.add() and sqr2.add() and sqr3.add() and sqr4.add() and sqr5.add() and sqr6.add() and sqr7.add() and sqr8.add() and sqr9.add():
        return True
    else: return False
