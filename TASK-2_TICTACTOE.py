# TIC TAC TOE 
# The board
def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to 3x3 Tic Tac Toe!")
    print("Player 1: X | Player 2: O")
    print("Note: Enter row and column numbers between 1 and 3.")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
            
            if row not in range(3) or col not in range(3):
                print("❗ Invalid position! Enter values between 1 and 3.")
                continue
            if board[row][col] != " ":
                print("❗ Cell already taken. Try again!")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break
            if is_draw(board):
                print("🤝 It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("❗ Please enter valid numeric input.")
            continue

if __name__ == "__main__":
    play_game()