from terminal import is_terminal
from minimax import minimax, get_valid_locations, drop_piece, get_next_open_row

class Main:

    def run(self):
        board = self.create_connect_four_board()
        current_player = 'R'  # Start with player Red
        while True:
            self.print_board(board)
            if current_player == 'R':
                column = self.get_human_move(board, current_player)
            else:
                column = self.get_ai_move(board)

            if not self.place_piece(board, column, current_player):
                print("Column is full. Try another one.")
                continue

            if is_terminal(board):
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
        row = get_next_open_row(board, column)
        if row is not None:
            drop_piece(board, row, column, player_color)
            return True
        return False

    def get_human_move(self, board, current_player):
        while True:
            try:
                column = int(input(f"Player {current_player}, choose a column (0-6): "))
                if column < 0 or column > 6:
                    raise ValueError
                if column not in get_valid_locations(board):
                    print("Column is full. Try another one.")
                    continue
                return column
            except ValueError:
                print("Invalid column. Please choose a number between 0 and 6.")

    def get_ai_move(self, board):
        column, minimax_score = minimax(board, 5, -float('inf'), float('inf'), True)
        print(f"AI chooses column {column}")
        return column


if __name__ == "__main__":
    main = Main()
    main.run()
