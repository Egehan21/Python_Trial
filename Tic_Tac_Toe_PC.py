import random

def print_board(board):
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print("---+---+---")
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print("---+---+---")
    print(f" {board['7']} | {board['8']} | {board['9']} ")

def user_moves():
    global board
    user_move= input("Please include your move: ")
    if int(user_move)>10 or int(user_move) <1 or board[user_move] != ' ':
            print("That is not possible, try again!")
            return user_move
    else:
            board[user_move]= user_x
            turn+=1
            print_board(board)
            return check_winner()

def computer_moves():
     global board
     available_moves = [key for key in board.keys() if board[key] == ' ']
     computer_move=random.choice(available_moves)
     board[computer_move]=user_y
     print_board(board)
     return check_winner()

def moves ():
    global board
    board = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '}
    turn = 0
    global user_x
    global user_y
    user_x = "X"
    user_y = "O"
    print_board(board)
    while turn < 9:
        if turn % 2 == 0:
            if user_moves():
                break
        else:
            if computer_moves():
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