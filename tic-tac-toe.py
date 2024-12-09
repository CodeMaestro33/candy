import random

def print_board(board):
    for i in range(3):
        print(' | '.join(board[i]))
        if i < 2:
            print('---------')

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def ai_move(board):
    empty_positions = get_empty_positions(board)
    return random.choice(empty_positions)

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    current_player = 'X'

    for _ in range(9):
        print_board(board)
        if current_player == 'X':
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
        else:
            print(f"AI's move:")
            row, col = ai_move(board)
        
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    print("It's a tie!")

tic_tac_toe()
