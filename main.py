class DrawMorpion:
    def __init__(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]

    def IsEmpty(self):
        return True



    def CreateBoard(self):
        print(f"{self.board[0]}{self.board[1]}{self.board[2]}")
        print(f"{self.board[3]}{self.board[4]}{self.board[5]}")
        print(f"{self.board[6]}{self.board[7]}{self.board[8]}")



board = DrawMorpion()

board.CreateBoard()