# Sudoku Solver in python.
class Solver(object):
    def __init__(self, board):
        self.board = board

    #Finds the next empty space.
    def findSpace(self):
        for i in range(9):
            for x in range(9):
                if self.board[i][x] == 0: return (i, x)
        return False
    
    #Checks the puzzle to see if it is solved.
    def checkBoard(self, number, position):
        #Check Rows
        for i in range(9):
            if position[1] != i and self.board[position[0]][i] == number:
                return False
        #Check Columns
        for i in range(9):
            if position[0] != i and self.board[i][position[1]] == number:
                return False
        #Check Boxes
        y = position[0] // 3
        x = position[1] // 3
        for i in range(y * 3, y * 3 + 3):
            for c in range(x * 3, x * 3 + 3):
                if position != (i,c) and self.board[i][c] == number:
                    return False
        #Returns True if the board is solved.
        return True
    
    #Solves the puzzle using backtracking algorithim. 
    def solver(self):
        get_space = self.findSpace()
        if get_space == False: return True
        else: r, c = self.findSpace()

        for i in range(1, 10):
            if self.checkBoard(i, (r, c)):
                self.board[r][c] = i
                if self.solver(): return True
                board[r][c] = 0
        return False
    
    #Main Loop.
    def main(self):
        self.solver()
        for i in self.board: print(i)

#Puzzle to be solved. Zeros are blank spaces.
board = [
[5, 0, 0, 0, 0, 0, 0, 7, 0],
[0, 2, 0, 0, 0, 6, 0, 0, 5],
[4, 0, 3, 0, 7, 0, 2, 1, 6],
[0, 0, 4, 0, 3, 0, 0, 0, 2],
[0, 0, 0, 1, 0, 2, 0, 0, 0],
[2, 0, 0, 0, 5, 0, 3, 0, 0],
[1, 8, 9, 0, 6, 0, 5, 0, 3],
[3, 0, 0, 8, 0, 0, 0, 6, 0],
[0, 4, 0, 0, 0, 0, 0, 0, 9]
]

#Solve Puzzle
if __name__ == "__main__":
    solver = Solver(board)
    solver.main()
