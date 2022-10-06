import random
from tkinter import Y
board = [['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']]
done = False
print("Welcome to Tic-Tac-Toe! You are X, Computer is O. You go first.")
count = 0
while(done!=True):
    print("BOARD \n")
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j], end = " ")
        print()
    print("\n")
    row = int(input("Enter row:"))
    column = int(input("Enter column:"))
    if(row<=2 and row>=0 and column<=2 and column>=0 and board[row][column]=="."):
        board[row][column]='X'
        count+=1
        count_row = 0
        for i in board[row]:
            if(i=='X'):
                count_row+=1
        count_col = 0
        if(board[0][column]=='X' and board[1][column]=='X' and board[2][column]=='X') or (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X'):
            count_col = 3
        diag = 0
        if(board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X'):
            diag = 3
        if(count_row==3 or count_col==3 or diag == 3):
            print("BOARD \n")
            for i in range(0,3):
                for j in range(0,3):
                    print(board[i][j], end = " ")
                print()
            print("\n")
            print("You win!")
            done = True
        if count == 9:
            print("BOARD \n")
            for i in range(0,3):
                for j in range(0,3):
                    print(board[i][j], end = " ")
                print()
            print("\n")
            print("It's a tie!")
            done = True
        else:
            crow = random.randint(0,2)
            ccol = random.randint(0,2)
            while(board[crow][ccol]!='.'):
                crow = random.randint(0,2)
                ccol = random.randint(0,2)
            board[crow][ccol]='O'
            count+=1
            count_row = 0
            for i in board[crow]:
                if(i=='O'):
                    count_row+=1
            count_col = 0
            if(board[0][ccol]=='O' and board[1][ccol]=='O' and board[2][ccol]=='O'):
                count_col = 3
            if(board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O') or (board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O'):
                diag = 3
            if(count_row==3 or count_col==3 or diag == 3):
                print("BOARD \n")
                for i in range(0,3):
                    for j in range(0,3):
                        print(board[i][j], end = " ")
                    print()
                print("\n")
                print("You lose :(")
                done = True
    else:
        print("Invalid position. Try again!")
