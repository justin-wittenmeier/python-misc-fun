#puzzle board
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

#get empty space
def emptySpace():
    for i in range(9):
        for x in range(9):
            if board[i][x] == 0: return (i, x)
    return False

#review board
def review(n, pos):
    #reviews rows
    for i in range(9):
        if pos[1] != i and board[pos[0]][i] == n: return False
    
    #reviews cols
    for i in range(9):
        if pos[0] != i and board[i][pos[1]] == n: return False
    
    #reviews boxes
    y = pos[0] // 3
    x = pos[1] // 3

    for i in range(y * 3, y * 3 + 3):
        for c in range(x * 3, x * 3 + 3):
            if pos != (i,c) and board[i][c] == n: return False
        
    return True

#solves puzzle
def solve():

    get_space = emptySpace()
    
    if get_space == False: return True
    else: r, c = get_space

    for i in range(1,10):
        if review(i, (r, c)):
            board[r][c] = i
            
            if solve(): return True

            board[r][c] = 0

    return False

#solve and print solved puzzle
solve()
for i in board: print(i)
