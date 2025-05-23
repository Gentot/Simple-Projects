#Tic-Tac-Toe
def print_board(board):
     for i in range(3):
        for j in range(3):
            if j < 2:
                print(board[i][j],end=" | ")
            else:
                print(board[i][j])
        if i<2:
            print("---------------")

        print()

def checktie(board):
    # Check if the board is full
    for row in board:
        if "   " in row:
            return False
    return True
        
def wincondition(board):
    #Check rows 
    if (board[0][0] == board[0][1] == board[0][2]) and board[0][0] != '   ' :
        return True
    elif (board[1][0] == board[1][1] == board[1][2]) and board[1][0] != '   ':
        return True
    elif (board[2][0] == board[2][1] == board[2][2]) and board[2][0] != '   ':
        return True
    #Check columns
    elif (board[0][0] == board[1][0] == board[2][0]) and board[0][0] != '   ':
        return True 
    elif (board[0][1] == board[1][1] == board[2][1]) and board[0][1] != '   ':
        return True 
    elif (board[0][2] == board[1][2] == board[2][2]) and board[0][2] != '   ':
        return True
    #check diagonals
    elif (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != '   ':
        return True
    elif (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != '   ':
        return True
    else:
        return False

def game():
    gameover=False
    board = [["   " for _ in range(3)] for _ in range(3)]
    rounds=1
    while not gameover:
        print_board(board)
        if rounds%2==1:
            #Player 1 turn
            while True:
                row=input("User 1 input row number 1-3: ")
                col=input("User 1 input column number 1-3: ")
                if (row == "" or col == ""):
                    print("Please enter a number")
                try:
                    row = int(row)
                    col = int(col)
                    if (col<=3 and col>= 1) and (row>=1 and row<=3) :
                        if board[row-1][col-1]=="   ":
                            board[row-1][col-1]=" X "
                            rounds +=1
                            break
                        else:
                            print("This tile is filled")
                            continue
                    else:
                        print("Input number 1,2, or 3 and column number 1,2, or 3")
                        continue
                except ValueError:
                        print("Invalid input, numbers only")
                        continue
                    
            if(wincondition(board)):
                print_board(board)
                print("User 1 wins")
                gameover=True
            elif checktie(board):
                print("It's a tie!")
                gameover=True
            else:
                gameover=False
                
        else:
            #Player 2 turn
            while True:
                row=input("User 2 input row number 1-3: ")
                col=input("User 2 input column number 1-3: ")
                if (row == "" or col == ""):
                    print("Please enter a number")
                try:
                    row = int(row)
                    col = int(col)
                    if (col<=3 and col>= 1) and (row>=1 and row<=3) :
                        if board[row-1][col-1]=="   ":
                            board[row-1][col-1]=" O "
                            rounds +=1
                            break
                        else:
                            print("This tile is filled")
                            continue
                    else:
                        print("Input number 1,2, or 3 and column number 1,2, or 3")
                        continue
                except ValueError:
                        print("Invalid input, numbers only")
                        continue
                
            if(wincondition(board)):
                print_board(board)
                print("User 2 wins")
                gameover=True
            elif checktie(board):
                print("It's a tie!")
                gameover=True
            else:
                gameover=False

    print("Thanks for Playing!!!")
    while True:
        print("Wanna play again? (y/n)")
        playagain=input()
        if playagain=="y":
            game()
        elif playagain=='n':
            print("Goodbye")
            break
        else:
            print("Invalid input, please enter y or n")
            continue

def main():
    print("Welcome to Tic Tac Toe")
    print("You are User 1 and you will be X")
    print("User 2 will be O")
    print("You will play first")
    game()

main()