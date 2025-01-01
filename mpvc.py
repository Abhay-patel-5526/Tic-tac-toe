import random

board=[7,8,9,4,5,6,1,2,3]  
board2=[1,2,3,4,5,6,7,8,9]                     
player_board=set()
com_board=set()
displayboard=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
#player win
def win_(player_board):
    victory=False
    c1,c2,c3,c4,c5,c6,c7,c8={1,2,3},{4,5,6},{7,8,9},{7,4,1},{8,5,2},{9,6,3},{1,5,9},{7,5,3} #win
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
        return True
victory=False
m=0
co=1

def display (b):
    print(f"{b[0]} | {b[1]} | {b[2]}\n{b[3]} | {b[4]} | {b[5]}\n{b[6]} | {b[7]} | {b[8]}")

def computer_move(com_board,player_board,rest_move):
    b=[{1,2,3},{4,5,6},{7,8,9},{7,4,1},{8,5,2},{9,6,3},{1,5,9},{7,5,3}]
    victory="not"
    c=set(com_board)
    p=set(player_board)
    r=set(rest_move)
    for a in b:
        d=a-c
        if d.issubset(r):
            if len(d)==1:
                victory="i don"
                return list(d)[0]
            else:
                print("hhh")
                victory=None
    if victory==None:
        for a in b:
            d=a-p
            if d.issubset(r):
                if len(d)==1:
                    victory="i don" 
                    return list(d)[0]
                else:
                    victory=None
    if victory==None:
        r=list(r)
        return random.choice(r)


#game mode
while True:
    chance=input("choose your symbol:'X' or 'O' :")
    print("Chart is:")
    display(board)

    if chance=='X':
            #player chance 1
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)

            #com chance 1
        print("computer's turn:")
        chance2=random.choice(board2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)
        chance2=None

        #player chance 2
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        
        #com chance 2
        chance2=computer_move(com_board,player_board,board2)
        print(chance2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)
        # chance2=None

        #player chance 3
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        victory=win_(player_board)
        if victory==True:
            print("You W I N !")
            break

        #com chance 3
        chance2=computer_move(com_board,player_board,board2)
        print(chance2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)
        chance2=None
        victory=win_(com_board)
        if victory==True:
            print("You L O S E !")
            break

        #player chance 4
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        victory=win_(player_board)
        if victory==True:
            print("You W I N !")
            break
        
        #com chance 4
        chance2=computer_move(com_board,player_board,board2)
        print(chance2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)
        chance2=None
        victory=win_(com_board)
        if victory==True:
            print("You L O S E !")
            break

        #player chance 5
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        victory=win_(player_board)
        if victory==True:
            print("You W I N !")
            break
        else:
            print("Game is D R A W!")

    

    if chance=='O':
        #com chance 1
        print("computer's turn:")
        chance2=random.choice(board2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)
        chance2=None

        #player chance 1
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        
        #com chance 2
        chance2=computer_move(com_board,player_board,board2)
        print(chance2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)

        #player chance 2
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        victory=win_(player_board)
        if victory==True:
            print("You W I N !")
            break

        #com chance 3
        chance2=computer_move(com_board,player_board,board2)
        print(chance2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)
        chance2=None
        victory=win_(com_board)
        if victory==True:
            print("You L O S E !")
            break

        #player chance 3
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        victory=win_(player_board)
        if victory==True:
            print("You W I N !")
            break
        
        #com chance 4
        chance2=computer_move(com_board,player_board,board2)
        print(chance2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)
        chance2=None
        victory=win_(com_board)
        if victory==True:
            print("You L O S E !")
            break

        #player chance 4
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        victory=win_(player_board)
        if victory==True:
            print("You W I N !")
            break

        #com chance 5
        chance2=computer_move(com_board,player_board,board2)
        print(chance2)
        com_board.add(chance2)
        displayboard[board.index(chance2)]="O"
        board[board.index(chance2)]="O"
        board2.remove(chance2)
        display(displayboard)
        if victory==True:
            print("You W I N !")
            break
        else:
            print("Game is D R A W!")