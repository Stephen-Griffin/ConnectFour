class Main:
    def __init__(self):
        this.self = self

    def run(self):
        # Add your code logic here
        board = self.create_connect_four_board()
        self.print_board(board)

    def create_connect_four_board(self):
        # Create a 6x7 Connect Four board with red and yellow colors
        board = [[' ' for _ in range(7)] for _ in range(6)]
        for row in range(6):
            for col in range(7):
                if (row + col) % 2 == 0:
                    board[row][col] = 'R'  # Red color
                else:
                    board[row][col] = 'Y'  # Yellow color
        return board

    def print_board(self, board):
        # Print the Connect Four board
        for row in board:
            print(' '.join(row))

if __name__ == "__main__":
    main = Main()
    main.run()