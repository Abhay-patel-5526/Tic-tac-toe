#tic tac toe
player1=input("Enter X player's name:")
player2=input("enter O  player's name:")

board=[7,8,9,4,5,6,1,2,3]                       
player1_board=set()
player2_board=set()
displayboard=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

#function to print board
def display (b):
    print(f"{b[0]} | {b[1]} | {b[2]}\n{b[3]} | {b[4]} | {b[5]}\n{b[6]} | {b[7]} | {b[8]}")

#function to win
c1,c2,c3,c4,c5,c6,c7,c8={1,2,3},{4,5,6},{7,8,9},{7,4,1},{8,5,2},{9,6,3},{1,5,9},{7,5,3}   #condition to win
victory=False


print("Chart is:")
display(board)
n=5
for a in range(0,n):
    chance1=int(input("enter where you want to turn your 'X':"))
    if chance1 in  board:
        player1_board.add(chance1)
        displayboard[board.index(chance1)]="X"
        board[board.index(chance1)]="X"
    else:
        n+=1
        print("invalid input")
        continue

    display(displayboard)

    if c1.issubset(player1_board):
        victory=True
    elif c2.issubset(player1_board):
        victory=True
    elif c3.issubset(player1_board):
        victory=True
    elif c4.issubset(player1_board):
        victory=True
    elif c5.issubset(player1_board):
        victory=True
    elif c6.issubset(player1_board):
        victory=True
    elif c7.issubset(player1_board):
        victory=True
    elif c8.issubset(player1_board):
        victory=True
    if  victory==True:
        print(f"{player1} wins")
        break

    if (a==4):
        print("game is draw")
        break
    chance2=int(input("enter where you want to turn your 'O':"))
    if chance2 in  board:
        player2_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
    else:
        n+=1
        print("invalid input")
        continue

    display(displayboard)

    if c1.issubset(player2_board):
        victory=True
    elif c2.issubset(player2_board):
        victory=True
    elif c3.issubset(player2_board):
        victory=True
    elif c4.issubset(player2_board):
        victory=True
    elif c5.issubset(player2_board):
        victory=True
    elif c6.issubset(player2_board):
        victory=True
    elif c7.issubset(player2_board):
        victory=True
    elif c8.issubset(player2_board):
        victory=True
    if  victory==True:
        print(f"{player2} wins")
        break