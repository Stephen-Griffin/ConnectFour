# Functional class that defines whether or not the board position is in the END state.
# This is determined by a win, or tie if the board is filled

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
            
    # checking sloped up 
    for col in range(4):
        for row in range(3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != 0:
                return True
            
    # checking sloped down 
    for col in range(4):
        for row in range(3, 6): 
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != 0:
                return True
            
    # if board is full, return false
    if any(0 in row for row in board):
        return False
    
    return False