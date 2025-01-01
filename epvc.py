import random

board=[7,8,9,4,5,6,1,2,3]  
board2=[1,2,3,4,5,6,7,8,9]                     
player_board=set()
com_board=set()
displayboard=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
victory=False

def display (b):
    print(f"{b[0]} | {b[1]} | {b[2]}\n{b[3]} | {b[4]} | {b[5]}\n{b[6]} | {b[7]} | {b[8]}")

c1,c2,c3,c4,c5,c6,c7,c8={1,2,3},{4,5,6},{7,8,9},{7,4,1},{8,5,2},{9,6,3},{1,5,9},{7,5,3} #win
n=5

#game mode
chance=input("choose your symbol:'X' or 'O' :")

print("Chart is:")
display(board)

#game mode X start
if chance=='X':
    for a in range(n):
        chance1=int(input("enter where you want to turn your 'X':"))
        if chance1 in  board:
            player_board.add(chance1)
            displayboard[board.index(chance1)]="X"
            board[board.index(chance1)]="X"
            board2.remove(chance1)
        else:
            n+=1
            print("invalid input")
            continue
        if c1.issubset(player_board):
            victory=True
        elif c2.issubset(player_board):
            victory=True
        elif c3.issubset(player_board):
            victory=True
        elif c4.issubset(player_board):
            victory=True
        elif c5.issubset(player_board):
            victory=True
        elif c6.issubset(player_board):
            victory=True
        elif c7.issubset(player_board):
            victory=True
        elif c8.issubset(player_board):
            victory=True
        if  victory==True:
            print("player wins")
            display(displayboard)
            break

        
        display(displayboard)
        
        #for computer
        if a==4:
            print("game is draw")
            break
        print("computer's chance")
        chance2=random.choice(board2
        )
        if chance2 in  board:
            com_board.add(chance2)
            displayboard[board.index(chance2)]="O"
            board[board.index(chance2)]="O"
            board2.remove(chance2)
        else:
            n+=1
            print("invalid input")
            continue

        display(displayboard)

        if c1.issubset(com_board):
            victory=True
        elif c2.issubset(com_board):
            victory=True
        elif c3.issubset(com_board):
            victory=True
        elif c4.issubset(com_board):
            victory=True
        elif c5.issubset(com_board):
            victory=True
        elif c6.issubset(com_board):
            victory=True
        elif c7.issubset(com_board):
            victory=True
        elif c8.issubset(com_board):
            victory=True
        if  victory==True:
            print("Computer wins")
            break


elif chance=='O':
    for a in range(n):
        print("computer's chance")
        chance2=random.choice(board2)
        if chance2 in  board:
            com_board.add(chance2)
            displayboard[board.index(chance2)]="X"
            board[board.index(chance2)]="X"
            board2.remove(chance2)
        else:
            n+=1
            print("invalid input")
            continue

        display(displayboard)

        if c1.issubset(com_board):
            victory=True
        elif c2.issubset(com_board):
            victory=True
        elif c3.issubset(com_board):
            victory=True
        elif c4.issubset(com_board):
            victory=True
        elif c5.issubset(com_board):
            victory=True
        elif c6.issubset(com_board):
            victory=True
        elif c7.issubset(com_board):
            victory=True
        elif c8.issubset(com_board):
            victory=True
        if  victory==True:
            print("Computer wins")
            break

        #for player
        if a==4:
            print("game is draw")
            break
        chance1=int(input("enter where you want to turn your 'O':"))
        if chance1 in  board:
            player_board.add(chance1)
            displayboard[board.index(chance1)]="O"
            board[board.index(chance1)]="O"
            board2.remove(chance1)
        else:
            n+=1
            print("invalid input")
            continue
        display(displayboard)
        if c1.issubset(player_board):
            victory=True
        elif c2.issubset(player_board):
            victory=True
        elif c3.issubset(player_board):
            victory=True
        elif c4.issubset(player_board):
            victory=True
        elif c5.issubset(player_board):
            victory=True
        elif c6.issubset(player_board):
            victory=True
        elif c7.issubset(player_board):
            victory=True
        elif c8.issubset(player_board):
            victory=True
        if  victory==True:
            print("player wins")
            break        