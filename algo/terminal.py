def winning_move(board, player):
    # Checking vertical win possibility 
    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
            
    # Checking horizontal win possibility
    for col in range(4):
        for row in range(6):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
            
    # Checking positively sloped diagonal win
    for col in range(4):
        for row in range(3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
            
    # Checking negatively sloped diagonal win
    for col in range(4):
        for row in range(3, 6):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True
            
    # If none are winning moves, return False
    return False

def is_terminal(board):
    for player in ['R', 'Y']:
        if winning_move(board, player):
            return True
    # Check for a full board (tie)
    if all(board[row][col] != ' ' for row in range(6) for col in range(7)):
        return True
    return False