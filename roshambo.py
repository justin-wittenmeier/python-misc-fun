import random

#Roshambo update.
class Game:
    def __init__(self):
        #List of moves.
        self.moves = ['rock','paper','scissors']
        #Selects a move at random for the bot. 
        self.botChoice = lambda: random.choice(self.moves)
    
    #Gets the players move.
    def playerChoice(self):
        #Get the first letter from each input to allow for easier play.
        alt_inputs = [i[0] for i in self.moves]
        #Get move from player.
        move = input('1: Rock\n2: Paper\n3: Scissors\nSelect Move: ').lower()
        #Catch wrong inputs.
        if move not in self.moves and move not in alt_inputs:
            try:
                move = int(move) -1
            except ValueError:
                print('\nERROR: Please select a valid move.\n')
                return self.playerChoice()
            if 0 < move > 2:
                print('\nERROR: Please select a valid move.\n')
                return self.playerChoice()
            move = self.moves[move]
        #Alt Input Convert
        if move == 'r': move = self.moves[0]
        if move == 'p': move = self.moves[1]
        if move == 's': move = self.moves[2]
        return move
        
    #Check the winner and display results.
    def winCheck(self, player, bot):
        outcomes = [(self.moves[0], self.moves[2]),(self.moves[2], self.moves[1]), (self.moves[1], self.moves[0])]
        win_form = ['\nResults: Draw\n', '\nResults: Player Wins!\n', '\nResults: Computer Wins!\n']
        if player == bot: 
            print(win_form[0])
        else:
            for i in outcomes:
                if player == i[0]:
                    if bot == i[1]:
                        print(win_form[1])
                    else:
                        print(win_form[2])
    def main(self):
        self.winCheck(self.playerChoice(), self.botChoice())
                
#Run game.
if __name__ == "__main__":
    game = Game()
    game.main()
