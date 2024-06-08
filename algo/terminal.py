# Function returns true if board in terminal position (i.e next placement = win)
def is_terminal(board):
    # checking vertical win possibility 
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != 0:
                return True
            
    # checking horizontal win possibility
    for col in range(4):
        for row in range(6):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] != 0:
                return True
            
    # checking sloped (up and to the right)
    for col in range (4):
        for row in range(3):
            if board[row][col] == board[row][col]




# alpha-beta pruning algorithm 
def abp_minimax(board, depth, alpha, beta, max): NotImplemented