from terminal import is_terminal, winning_move

def evaluate_window(window, player):
    score = 0
    opp_player = 'Y' if player == 'R' else 'R'
    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(' ') == 1:
        score += 5
    elif window.count(player) == 2 and window.count(' ') == 2:
        score += 2

    if window.count(opp_player) == 3 and window.count(' ') == 1:
        score -= 4

    return score

def score_position(board, player):
    score = 0

    # Score center column
    center_array = [board[i][3] for i in range(6)]
    center_count = center_array.count(player)
    score += center_count * 3

    # Score Horizontal
    for r in range(6):
        row_array = [board[r][c] for c in range(7)]
        for c in range(4):
            window = row_array[c:c+4]
            score += evaluate_window(window, player)

    # Score Vertical
    for c in range(7):
        col_array = [board[r][c] for r in range(6)]
        for r in range(3):
            window = col_array[r:r+4]
            score += evaluate_window(window, player)

    # Score positive sloped diagonal
    for r in range(3):
        for c in range(4):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, player)

    # Score negative sloped diagonal
    for r in range(3):
        for c in range(4):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, player)

    return score

def get_valid_locations(board):
    valid_locations = []
    for col in range(7):
        if board[0][col] == ' ':
            valid_locations.append(col)
    return valid_locations

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_next_open_row(board, col):
    for r in range(5, -1, -1):
        if board[r][col] == ' ':
            return r

def is_terminal_node(board):
    return is_terminal(board)

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, 'R'):
                return (None, 100000000000000)
            elif winning_move(board, 'Y'):
                return (None, -10000000000000)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(board, 'R'))
    if maximizingPlayer:
        value = -float('inf')
        column = valid_locations[0]
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [row[:] for row in board]
            drop_piece(b_copy, row, col, 'R')
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else: # Minimizing player
        value = float('inf')
        column = valid_locations[0]
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [row[:] for row in board]
            drop_piece(b_copy, row, col, 'Y')
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value