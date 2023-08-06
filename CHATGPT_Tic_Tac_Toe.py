import random

def print_board(board):
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print("---+---+---")
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print("---+---+---")
    print(f" {board['7']} | {board['8']} | {board['9']} ")

def user_move():
    global board
    move = input("Include your place: ")
    if int(move) > 9 or int(move) < 1 or board[move] != ' ':
        print("That is not possible, try again!")
        return user_move()
    else:
        board[move] = user_x
        print_board(board)
        return check_winner()

def computer_move():
    global board
    available_moves = [key for key in board.keys() if board[key] == ' ']
    move = random.choice(available_moves)
    board[move] = user_y
    print(f"Computer chose {move}")
    print_board(board)
    return check_winner()

def moves():
    global board
    board = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
    }
    global user_x
    global user_y
    user_x = "X"
    user_y = "O"
    print_board(board)

    turn = 0
    while turn < 9:
        if turn % 2 == 0:
            if user_move():
                break
        else:
            if computer_move():
                break
        turn += 1
    else:
        print("It's a draw!")

def check_winner():
    winning_combinations = [
        ('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),  # Horizontal
        ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),  # Vertical
        ('1', '5', '9'), ('3', '5', '7')]  # Diagonals
    for combination in winning_combinations:
        a,b,c = combination
        if board[a] == board[b] == board [c] != ' ':
            print ("The winner is:", board[a])
            return True
        
    return False

moves()
