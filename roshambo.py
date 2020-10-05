import random

def roshambo():
    # valid moves
    moves = ['rock','paper','scissors']
    #bot move
    bot_choice = lambda :random.choice(moves)
    #player move
    def player_choice():
        alt_letter_inputs = ['r', 'p', 's']
        move = input('1: Rock\n2: Paper\n3: Scissors\nSelect Move: ').lower()

        if move not in moves and move not in alt_letter_inputs:
            try: 
                move = int(move) - 1
            except ValueError:
                print('\nERROR: Please select a valid move.\n')
                return player_choice()
            if 0 < move > 2:
                print('\nERROR: Please select a valid move.\n')
                return player_choice()
            move = moves[move]
        
        if move == 'r': move = moves[0]
        if move == 'p': move = moves[1]
        if move == 's': move = moves[2]

        return move
    #checks winner and dislplays results
    def win_check(p, b):
        if p == b: print('\nResults: Draw\n')
        elif p == moves[1] and b == moves[0]: print('\nResults: Player Wins!\n')
        elif p == moves[2] and b == moves[1]: print('\nResults: Player Wins!\n')
        elif p == moves[0] and b == moves[2]: print('\nResults: Player Wins!\n')
        elif b == moves[1] and p == moves[0]: print('\nResults: Computer Wins!\n')
        elif b == moves[2] and p == moves[1]: print('\nResults: Computer Wins!\n')
        elif b == moves[0] and p == moves[2]: print('\nResults: Computer Wins!\n')
        else: print(f'\n{b}\n')


    print('')

    win_check(player_choice(), bot_choice())

roshambo()
