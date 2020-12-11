#Tic Tak Toe Update
class Game(object):
    def __init__(self):
        #generate board
        self.board = [' '] * 9
        
        #turn tracker
        self.current_turn = 'O'

        #on/off switch
        self.game_on = False

    #cleans the board
    def clearBoard(self):
        self.board = [' '] * 9
    
    #prints the current board
    def printBoard(self): print(f'Current Board:\n{self.board[6]}|{self.board[7]}|{self.board[8]}\n-+-+-\n{self.board[3]}|{self.board[4]}|{self.board[5]}\n-+-+-\n{self.board[0]}|{self.board[1]}|{self.board[2]}')
    
    #prints info version of board
    def printInfoBoard(self): print('Select Move:\n7|8|9\n-+-+-\n4|5|6\n-+-+-\n1|2|3')

    #start game
    def startGame(self):
        input('Enter anything to start game: ')
        self.clearBoard()
        return True

    #checks turn
    def runGame(self):
        if self.current_turn == 'O': self.playerMove()
        elif self.current_turn == 'X': self.botMove()

    #checks if game is over
    def gameOver(self):
        if self.board[0] == self.board[1] == self.board[2] != ' ':
            self.printBoard()
            print(f'\nWINNER: {self.board[0]}')
            self.current_turn = self.board[0]
            return False
        elif self.board[3] == self.board[4] == self.board[5] != ' ':
            self.printBoard()
            print(f'\nWINNER: {self.board[3]}')
            self.current_turn = self.board[3]
            return False
        elif self.board[6] == self.board[7] == self.board[8] != ' ':
            self.printBoard()
            print(f'\nWINNER: {self.board[6]}')
            self.current_turn = self.board[6]
            return False
        elif self.board[2] == self.board[4] == self.board[6] != ' ':
            self.printBoard()
            print(f'\nWINNER: {self.board[6]}')
            self.current_turn = self.board[6]
            return False
        elif self.board[0] == self.board[4] == self.board[8] != ' ':
            self.printBoard()
            print(f'\nWINNER: {self.board[0]}')
            self.current_turn = self.board[0]
            return False
        elif self.board[0] == self.board[3] == self.board[6] != ' ':
            self.printBoard()
            print(f'\nWINNER: {self.board[0]}')
            self.current_turn = self.board[0]
            return False
        elif self.board[1] == self.board[4] == self.board[7] != ' ':
            self.printBoard()
            print(f'\nWINNER: {self.board[1]}')
            self.current_turn = self.board[1]
            return False
        elif self.board[2] == self.board[5] == self.board[8] != ' ':
            self.printBoard()
            print(f'\nWINNER: {self.board[2]}')
            self.current_turn = self.board[2]
            return False
        elif ' ' not in self.board:
            self.printBoard()
            print('\nDRAW\n')
            return False
        else: return True
    
    #player move
    def playerMove(self):
        self.printBoard()
        print()
        self.printInfoBoard()
        print(f'Current Turn: {self.current_turn}')
        move = input('Select Square: ')
        try: move = int(move)
        except ValueError:
            print('\nError: Please only enter numbers\n')
            return self.playerMove()
        move -= 1
        if move > 8 or move < 0:
            print('\nERROR: please only select numbers between 1 and 9\n')
            return self.playerMove()
        if self.board[move] in 'XO':
            print('\nERROR: Space occupied please try again\n')
            return self.playerMove()
        
        self.board[move] = 'O'

        self.current_turn = 'X'
    
    #bot move
    def botMove(self):

        def gameOverBot():
            if self.board[0] == self.board[1] == self.board[2] != ' ': return self.board[0]
            elif self.board[3] == self.board[4] == self.board[5] != ' ': return self.board[3]
            elif self.board[6] == self.board[7] == self.board[8] != ' ': return self.board[6]
            elif self.board[2] == self.board[4] == self.board[6] != ' ': return self.board[2]
            elif self.board[0] == self.board[4] == self.board[8] != ' ': return self.board[0]
            elif self.board[0] == self.board[3] == self.board[6] != ' ': return self.board[0]
            elif self.board[1] == self.board[4] == self.board[7] != ' ': return self.board[1]
            elif self.board[2] == self.board[5] == self.board[8] != ' ': return self.board[2]
            elif ' ' not in self.board: return '--'
            else: return None
        
        def max(a, b):
            
            maxi = -2
            move = None
            results = gameOverBot()
            
            if results == 'O': return [-1, 0]
            elif results == 'X': return [2, 0]
            elif results == '--': return [0, 0]
            
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    m = min(a, b)

                    if m[0] > maxi:
                        maxi = m[0]
                        move = i
                    
                    self.board[i] = ' '

                    if maxi >= b: return [maxi, move]
                    if maxi > a: a = maxi

            return [maxi, move]
            
        def min(a, b):
            
            mini = 2
            move = None
            results = gameOverBot()

            if results == 'O': return [-1, 0]
            elif results == 'X': return [1, 0]
            elif results == '--': return [0, 0]

            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    m = max(a, b)

                    if m[0] < mini:
                        mini = m[0]
                        move = i
                    
                    self.board[i] = ' '

                    if mini <= a: return [mini, move]
                    if mini < b: b = mini
            
            return [mini, move]
        
        r = max(-2, 2)
        

        self.board[r[1]] = 'X'
        
        self.current_turn = 'O'

#runs the game on a loop
game = Game()

while True:
    game.game_on = game.startGame()
    while game.game_on:
        game.runGame()
        game.game_on = game.gameOver()
        
