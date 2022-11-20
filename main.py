class DrawMorpion:
    def __init__(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]

    def CreateBoard(self):
        print(f"{self.board[0]}{self.board[1]}{self.board[2]}")
        print(f"{self.board[3]}{self.board[4]}{self.board[5]}")
        print(f"{self.board[6]}{self.board[7]}{self.board[8]}")

    def playerOne(self):
        isX = int(input("Entrez un numero entre 0 et 8: "))
        self.board[isX] = "X"

    def playerTwo(self):
        isO = int(input("Entrez un numero entre 0 et 8: "))
        self.board[isO] = "O"


board = DrawMorpion()

for i in range(9):
    board.CreateBoard()
    board.playerOne()
    board.CreateBoard()
    board.playerTwo()

