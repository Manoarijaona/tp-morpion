from case import Case
from states import CaseStates

class Board:
    def __init__(self):
        return

    def draw(self, caseStates: []):
        for i in range(3):
            for j in range(3):
                if caseStates[i*3 + j] == Case.isO:
                    print('O', end='')
                elif caseStates[i*3 + j] == Case.isX:
                    print('X', end='')
                else:
                    print(' ', end='')
                if j < 2:
                    print('|', end='')
            print()
            if i < 2:
                print('-----')
        print()

board = Board()
board.draw([Case.isEmpty,Case.isEmpty,Case.isEmpty,Case.isEmpty,Case.isEmpty,Case.isEmpty,Case.isEmpty,Case.isEmpty,Case.isEmpty,])
