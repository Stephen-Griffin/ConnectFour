from terminal import is_terminal

class Main:

    def run(self):
        board = self.create_connect_four_board()
        current_player = 'R'  # Start with player Red
        while True:
            self.print_board(board)
            try:
                column = int(input(f"Player {current_player}, choose a column (0-6): "))
                if column < 0 or column > 6:
                    raise ValueError
            except ValueError:
                print("Invalid column. Please choose a number between 0 and 6.")
                continue

            if not self.place_piece(board, column, current_player):
                print("Column is full. Try another one.")
                continue

            if self.check_win(board, current_player):
                self.print_board(board)
                print(f"Player {current_player} wins!")
                break

            current_player = 'Y' if current_player == 'R' else 'R'  # Switch players

    def create_connect_four_board(self):
        return [[' ' for _ in range(7)] for _ in range(6)]

    def print_board(self, board):
        for row in board:
            print(' '.join(row))
        print('0 1 2 3 4 5 6')  # Column numbers

    def place_piece(self, board, column, player_color):
        for row in reversed(range(6)):
            if board[row][column] == ' ':
                board[row][column] = player_color
                return True
        return False

    def check_win(self, board):
        return is_terminal(board);

if __name__ == "__main__":
    main = Main()
    main.run()