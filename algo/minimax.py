from ConnectFour.algo.terminal import is_terminal
from ConnectFour.algo.terminal import winning_move


# alpha-beta pruning algorithm for connect four
def abp_minimax(board, depth, alpha, beta, max): 
    if depth == 0 or is_terminal(board): 
        NotImplemented