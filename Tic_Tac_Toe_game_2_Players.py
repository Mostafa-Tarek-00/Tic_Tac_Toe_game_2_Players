# 1, 2, 3 || 4, 5, 6 || 7, 8, 9 ==>> win
# 1, 4, 7 || 2, 5, 8 || 3, 6, 9 ==>> win
# 1, 5, 9 ==>> win
# 3, 5, 7 ==>> win
print("Player 1 ==>> X")
print("Player 2 ==>> O")
print("Start")
def draw_board(board):
    print(f" {board[0]} ║ {board[1]} ║ {board[2]} ")
    print("═══╬═══╬═══")
    print(f" {board[3]} ║ {board[4]} ║ {board[5]} ")
    print("═══╬═══╬═══")
    print(f" {board[6]} ║ {board[7]} ║ {board[8]} ")

def check_win(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def check_draw(board):
    return all(cell == "X" or cell == "O" for cell in board)

def choose_position(board, player_symbol):
    while True:
        try:
            choice = int(input(f"Player {player_symbol} Choose a Position (1-9): "))
            if 1 <= choice <= 9 and board[choice - 1] != "X" and board[choice - 1] != "O":
                return choice - 1
            else:
                print("Invalid or Occupied Position. Choose Again.")
        except ValueError:
            print("Invalid Input. Please Enter a Number.")

def play_game():
    game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    draw_board(game_board)
    
    players = ["X", "O"]
    current_player = 0

    while True:
        position = choose_position(game_board, players[current_player])
        game_board[position] = players[current_player]
        draw_board(game_board)

        if check_win(game_board, players[current_player]):
            print(f"Player {players[current_player]} Wins!")
            break
        elif check_draw(game_board):
            print("It's a Draw!")
            break

        current_player = 1 - current_player

    replay = input("Do you want to play again? (yes/no): ")
    return replay.lower() == "yes"

def main():
    while True:
        if not play_game():
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
