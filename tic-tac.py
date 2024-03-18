def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    moves = 0

    print("Welcome to Tic-Tac-Toe!")

    while moves < 9:
        print_board(board)
        row = int(input("Player {} enter row number (0-2): ".format(players[current_player])))
        col = int(input("Player {} enter column number (0-2): ".format(players[current_player])))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = players[current_player]
        moves += 1

        if check_winner(board, players[current_player]):
            print_board(board)
            print("Player {} wins!".format(players[current_player]))
            break

        current_player = (current_player + 1) % 2

    if moves == 9:
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    main()
