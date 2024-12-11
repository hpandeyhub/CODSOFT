# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check if the board is full
def board_full():
    return ' ' not in board


# Function to check for a winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]             # Diagonal
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Minimax function
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if board_full():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


# Function to determine the AI move
def ai_move():
    best_score = float('-inf')
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'


# Function to get the human player's move
def human_move():
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Invalid move! Try again.")
        human_move()


# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("Congratulations, you win!")
            break
        if board_full():
            print("It's a tie!")
            break

        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if board_full():
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
