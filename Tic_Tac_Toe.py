def print_board(board):
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print("---+---+---")
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print("---+---+---")
    print(f" {board['7']} | {board['8']} | {board['9']} ")
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
    while turn <9:
        if turn %2==0:
            move_1=input("Include your place: ")
            if int(move_1)>10 or int(move_1) <1 or board[move_1] != ' ':
                print("That is not possible, try again!")
            else:
                    board[move_1]= user_x
                    turn+=1
                    print_board(board)
                    if check_winner():
                        break
        else:
            move_2=input("Include your place: ")
            if int(move_2)>10 or int(move_2) <1 or board[move_2] != ' ':
                print("That is not possible, try agai!")
            else:
                board[move_2]= user_y
                turn+=1
                print_board(board)
                if check_winner():
                    break
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