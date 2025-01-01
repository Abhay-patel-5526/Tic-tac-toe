board=[7,8,9,4,5,6,1,2,3]  
board2=[1,2,3,4,5,6,7,8,9]                     
player_board=set()
com_board=set()
displayboard=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
victory=False
m=0
co=1

def display (b):
    print(f"{b[0]} | {b[1]} | {b[2]}\n{b[3]} | {b[4]} | {b[5]}\n{b[6]} | {b[7]} | {b[8]}")


#game mode
chance=input("choose your symbol:'X' or 'O' :")
games=[[9,5,[8,7,[4,3,"v"],
             [1,3,"v"],
             [2,3,"v"],
             [3,6,[4,1],
                 [1,4,"v"],
                 [2,4,"v"]],
             [6,3,"v"]],
        [7,8,[4,2,"v"],
         [1,2,"v"],
         [2,6,[4,1],
             [1,4,"v"],
             [3,4,"v"]],
         [3,2,"v"],
         [6,2,"v"]],
        [4,7,[1,3,"v"],
         [2,3,"v"],
         [3,6,[8,2],
             [1,2],
             [2,1]],
         [6,3,"v"],
         [8,3,"v"]],
        [1,4,[2,6,"v"],
         [3,6,"v"],
         [6,3,[8,7,"v"],
             [7,8],
             [2,7,"v"]],
         [8,6,"v"],
         [7,6,"v"]],
        [2,4,[1,6,"v"],
         [3,6,"v"],
         [6,3,[8,7,"v"],
             [7,8],
             [1,7,"v"]],
         [8,6,"v"],
         [7,6,"v"]],
        [3,6,[8,4,"v"],
         [7,4,"v"],
         [4,2,[8,7],
             [7,8,"v"],
             [1,8,"v"]],
         [1,4,"v"],
         [2,4,"v"]],
        [6,3,[8,7,"v"],
         [7,8],
         [4,7,"v"],
         [1,7,"v"],
         [2,7,"v"]]],
    [8,5,[7,9,[4,1,"v"],
         [1,4,[2,6,"v"],
             [3,6,"v"],
             [6,2]],
         [2,1,"v"],
         [3,1,"v"],
         [6,1,"v"]],
     [4,7,[1,3,"v"],
         [2,3,"v"],
         [3,6,[1,2],
             [2,1],
             [9,1]],
         [6,3,"v"],
         [9,3,"v"]],
     [1,4,[2,6,"v"],
         [3,6,"v"],
         [6,7,[9,3,"v"],
             [3,9],
             [2,9,"v"]],
         [8,6,"v"],
         [7,6,"v"]],
     [2,4,[3,6,"v"],
         [6,7,[9,1,"v"],
             [3,1,"v"],
             [1,3,"v"]],
         [9,6,"v"],
         [7,6,"v"],
         [1,6,"v"]],
     [3,6,[9,4,"v"],
         [7,4,"v"],
         [4,9,[7,1,"v"],
             [1,7],
             [2,1,"v"]],
         [1,4,"v"],
         [2,4,"v"]],
     [6,9,[7,1,"v"],
         [4,1,"v"],
         [1,3,[7,4],
             [4,7,"v"],
             [3,2,"v"]],
         [2,1,"v"],
         [3,1,"v"]],
     [9,7,[4,3,"v"],
         [1,3,"v"],
         [2,3,"v"],
         [3,6,[4,1],
             [1,4,"v"],
             [2,4,"v"]],
         [6,3,"v"]]],
    [7,5,[4,1,[2,9,"v"],
         [3,9,"v"],
         [6,9,"v"],
         [9,8,[6,2,"v"],
             [3,2,"v"],
             [2,3]],
         [8,9,"v"]],
     [1,4,[2,6,"v"],
         [3,6,"v"],
         [6,8,[9,2,"v"],
             [3,2,"v"],
             [2,3]],
         [9,6,"v"],
         [8,6,"v"]],
     [2,4,[1,6,"v"],
         [3,6,"v"],
         [6,9,[8,1,"v"],
             [3,1,"v"],
             [1,3]],
         [9,6,"v"],
         [8,6,"v"]],
     [3,6,[9,4,"v"],
         [8,4,"v"],
         [4,1,[2,9,"v"],
             [8,9,"v"],
             [9,8]],
         [1,4,"v"],
         [2,4,"v"]],
     [6,9,[8,1,"v"],
         [4,1,"v"],
         [1,4,[8,2],
             [2,3],
             [3,2]],
         [2,1,"v"],
         [3,1,"v"]],
     [9,8,[4,2,"v"],
         [1,2,"v"],
         [2,6,[3,4,"v"],
             [1,4,"v"],
             [4,1]],
         [3,2,"v"],
         [6,2,"v"]],
     [8,9,[4,1,"v"],
         [1,4,[2,6,"v"],
             [3,6,"v"],
             [6,2]],
         [2,1,"v"],
         [3,1,"v"],
         [6,1,"v"]]],
    [4,5,[1,7,[2,3,"v"],
         [3,2,[6,8,"v"],
              [9,8,"v"],
              [8,9]],
         [6,3,"v"],
         [9,3,"v"],
         [8,3,"v"]],
     [2,1,[3,9,"v"],
         [6,9,"v"],
         [9,7,[8,3,"v"],
             [6,3,"v"],
             [3,6]],
         [8,9,"v"],
         [7,9,"v"]],
     [3,2,[6,8,"v"],
         [9,8,"v"],
         [8,9,[7,1,"v"],
             [6,1,"v"],
             [1,7]],
         [7,8,"v"],
         [1,8,"v"]],
     [6,9,[8,1,"v"],
         [7,1,"v"],
         [1,7,[8,3,"v"],
             [2,3,"v"],
             [3,2]],
         [2,1,"v"],
         [3,1,"v"]],
     [9,8,[7,2,"v"],
         [1,2,"v"],
         [2,7,[6,3,"v"],
             [1,3,"v"],
             [3,1]],
         [3,2,"v"],
         [4,2,"v"]],
     [8,7,[1,3,"v"],
         [2,3,"v"],
         [3,1,[2,9,"v"],
             [6,9,"v"],
             [9,6]],
         [6,1,"v"],
         [9,1,"v"]],
     [7,1,[2,9,"v"],
         [3,9,"v"],
         [6,9,"v"],
         [9,8,[6,2,"v"],
             [3,2,"v"],
             [2,3]],
         [8,9,"v"]]],
    [1,5,[2,3,[6,7,"v"],
         [9,7,"v"],
         [8,7,"v"],
         [7,4,[8,6,"v"],
             [9,6,"v"],
             [6,9]],
         [4,7,"v"]],
     [3,2,[6,8,"v"],
         [9,8,"v"],
         [8,4,[7,6,"v"],
             [9,6,"v"],
             [6,9]],
         [7,8,"v"],
         [4,8,"v"]],
     [6,3,[9,7,"v"],
         [8,7,"v"],
         [7,4,[2,8],
             [8,9],
             [9,8]],
         [4,7,"v"],
         [2,7,"v"]],
     [9,8,[7,2,"v"],
         [4,2,"v"],
         [2,3,[6,7,"v"],
             [4,7,"v"],
             [7,4]],
         [3,2,"v"],
         [6,2,"v"]],
     [8,7,[4,3,"v"],
         [2,3,"v"],
         [3,2,[4,6],
             [6,9],
             [9,6]],
         [6,3,"v"],
         [9,3,"v"]],
     [7,4,[2,6,"v"],
         [3,6,"v"],
         [6,8,[9,2,"v"],
             [3,2,"v"],
             [2,3]],
         [8,6,"v"],
         [9,6,"v"]],
     [4,7,[2,3,"v"],
         [3,2,[6,8,"v"],
             [9,8,"v"],
             [8,9]],
         [6,3,"v"],
         [9,3,"v"],
         [8,3,"v"]]],
    [2,5,[3,1,[6,9,"v"],
         [9,6,[8,4,"v"],
             [7,4,"v"],
             [4,7]],
         [8,9,"v"],
         [7,9,"v"],
         [4,9,"v"]],
     [6,3,[9,7,"v"],
         [8,7,"v"],
         [7,1,[4,9,"v"],
             [8,9,"v"],
             [9,8]],
         [4,7,"v"],
         [1,7,"v"]],
     [9,3,[6,7,"v"],
         [8,7,"v"],
         [7,8,[4,1],
             [1,4],
             [6,1]],
         [4,7,"v"],
         [1,7,"v"]],
     [8,7,[4,3,"v"],
         [1,3,"v"],
         [3,1,[4,9,"v"],
             [6,9,"v"],
             [9,6]],
         [6,3,"v"],
         [9,3,"v"]],
     [7,4,[1,6,"v"],
         [3,6,"v"],
         [6,9,[8,1,"v"],
             [3,1,"v"],
             [1,3]],
         [9,6,"v"],
         [8,6,"v"]],
     [4,1,[3,9,"v"],
         [6,9,"v"],
         [9,3,[6,7,"v"],
             [8,7,"v"],
             [7,8]],
         [8,9,"v"],
         [7,9,"v"]],
     [1,3,[6,7,"v"],
         [9,7,"v"],
         [8,7,"v"],
         [7,4,[8,6,"v"],
             [9,6,"v"],
             [6,9]],
         [4,7,"v"]]],
    [3,5,[6,9,[8,1,"v"],
         [7,1,"v"],
         [4,1,"v"],
         [1,2,[4,8,"v"],
             [7,8,"v"],
             [8,7]],
         [2,1,"v"]],
     [9,6,[8,4,"v"],
         [7,4,"v"],
         [4,2,[1,8,"v"],
             [7,8,"v"],
             [8,7]],
         [1,4,"v"],
         [2,4,"v"]],
     [8,9,[6,1,"v"],
         [7,1,"v"],
         [4,1,"v"],
         [1,2,[6,4],
             [7,4],
             [4,7]],
         [2,1,"v"]],
     [7,4,[1,6,"v"],
         [2,6,"v"],
         [6,9,[8,1,"v"],
             [2,1,"v"],
             [1,2]],
         [9,6,"v"],
         [8,6,"v"]],
     [4,1,[2,9,"v"],
         [6,9,"v"],
         [9,6,[8,7],
             [7,8],
             [2,8]],
         [8,9,"v"],
         [7,9,"v"]],
     [1,2,[6,8,"v"],
         [9,8,"v"],
         [8,6,[9,4,"v"],
             [7,4,"v"],
             [4,7]],
         [7,8,"v"],
         [4,8,"v"]],
     [2,1,[6,9,"v"],
         [9,6,[8,4,"v"],
             [7,4,"v"],
             [4,7]],
         [8,9,"v"],
         [7,9,"v"],
         [4,9,"v"]]],
    [6,5,[9,3,[8,7,"v"],
         [7,8,[4,2,"v"],
             [1,2,"v"],
             [2,1]],
         [4,7,"v"],
         [1,7,"v"],
         [2,7,"v"]],
     [8,9,[7,1,"v"],
         [4,1,"v"],
         [1,3,[2,7,"v"],
             [4,7,"v"],
             [7,4]],
         [2,1,"v"],
         [3,1,"v"]],
     [7,8,[9,2,"v"],
         [4,2,"v"],
         [1,2,"v"],
         [2,1,[3,9,"v"],
             [4,9,"v"],
             [9,3]],
         [3,2,"v"]],   
     [4,1,[2,9,"v"],
         [3,9,"v"],
         [9,3,[2,7,"v"],
             [8,7,"v"],
             [7,8]],
         [8,9,"v"],
         [7,9,"v"]],
     [1,2,[3,8,"v"],
         [9,8,"v"],
         [8,7,[4,3,"v"],
             [9,3,"v"],
             [3,9]],
         [7,8,"v"],
         [4,8,"v"]],
     [2,3,[9,7,"v"],
         [8,7,"v"],
         [7,1,[4,9,"v"],
             [8,9,"v"],
             [9,8]],
         [4,7,"v"],
         [1,7,"v"]],
     [3,9,[8,1,"v"],
         [7,1,"v"],
         [4,1,"v"],
         [1,2,[4,8,"v"],
             [7,8,"v"],
             [8,7,]],
         [2,1,"v"]]],
    [5,9,[8,2,[7,3,[4,1,"v"],
             [1,6,"v"],
             [6,1,"v"]],
         [4,6,[7,3,"v"],
             [1,3,"v"],
             [3,7]],
         [1,3,[7,6,"v"],
             [4,6,"v"],
             [6,7]],
         [3,7,[4,6],
             [1,6],
             [6,4]],
         [6,4,[7,3],
             [1,3],
             [3,7]]],
     [7,3,[8,6,"v"],
         [4,6,"v"],
         [1,6,"v"],
         [2,6,"v"],
         [6,4,[8,2],
             [1,2],
             [2,8]]],
     [4,6,[8,3,"v"],
         [7,3,"v"],
         [1,3,"v"],
         [2,3,"v"],
         [3,7,[1,8,"v"],
             [2,8,"v"],
             [8,2]]],
     [1,3,[8,6,"v"],
         [7,6,"v"],
         [4,6,"v"],
         [2,6,"v"],
         [6,4,[8,2],
             [7,2],
             [2,8]]],
     [2,8,[4,7,"v"],
         [1,7,"v"],
         [3,7,"v"],
         [6,7,"v"],
         [7,3,[4,6,"v"],
             [1,6,"v"],
             [6,4]]],
     [3,7,[4,8,"v"],
         [1,8,"v"],
         [2,8,"v"],
         [6,8,"v"],
         [8,2,[4,6,],
             [1,6],
             [6,4]]],
     [6,4,[8,2,[7,3],
             [1,3],
             [3,7]],
         [7,3,[8,2],
             [1,2],
             [2,8]],
         [1,7,[3,8,"v"],
             [2,8,"v"],
             [8,2]],
         [2,8,[3,7,"v"],
             [1,7,"v"],
             [7,3]],
         [3,7,[8,2],
             [1,8,"v"],
             [2,8,"v"]]]]
]
row=[]
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
    for a in games:
        if a[0]==chance1:
            chance2=a[1]
            com_board.add(chance2)
            displayboard[board.index(chance2)]="O"
            board[board.index(chance2)]="O"
            board2.remove(chance2)
            row=a
            row.pop(0)
            row.pop(0)

    display(displayboard)

    co=1
        #player chance 2
    for a in range(co):
        chance1=int(input("enter where you want to turn your 'X':"))
        if chance1 in  board:
            player_board.add(chance1)
            displayboard[board.index(chance1)]="X"
            board[board.index(chance1)]="X"
            board2.remove(chance1)
        else:
            print("invalid input")
            co-=1
    display(displayboard)

    #com chance 2
    print("computer's turn:")
    for a in row:
        if a[0]==chance1:
            chance2=a[1]
            com_board.add(chance2)
            displayboard[board.index(chance2)]="O"
            board[board.index(chance2)]="O"
            board2.remove(chance2)
            row=a
            row.pop(0)
            row.pop(0)

    display(displayboard)
    co=1
        #player chance 3
    for a in range(co):
        chance1=int(input("enter where you want to turn your 'X':"))
        if chance1 in  board:
            player_board.add(chance1)
            displayboard[board.index(chance1)]="X"
            board[board.index(chance1)]="X"
            board2.remove(chance1)
        else:
            print("invalid input")
            co-=1
    display(displayboard)

    #com chance 3
    print("computer's turn:")
    for a in row:
        if a[0]==chance1:
            chance2=a[1]
            com_board.add(chance2)
            displayboard[board.index(chance2)]="O"
            board[board.index(chance2)]="O"
            board2.remove(chance2)
            if len(a)==3:
                victory=True
            row=a
            row.pop(0)
            row.pop(0)
    display(displayboard)
    if victory==True:
        print("Oops! You  L O S E !")
    else:
        #player chance 4
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in  board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        #com chance 4
        for a in row:
            if a[0]==chance1:
                chance2=a[1]
                com_board.add(chance2)
                displayboard[board.index(chance2)]="O"
                board[board.index(chance2)]="O"
                board2.remove(chance2)
                if len(a)==3:
                    victory=True
                row=a
                row.pop(0)
                row.pop(0)
        display(displayboard)
        if victory==True:
            print("Oops! You  L O S E !")
        else:
            #player chance 5
            for a in range(co):
                chance1=int(input("enter where you want to turn your 'X':"))
                if chance1 in  board:
                    player_board.add(chance1)
                    displayboard[board.index(chance1)]="X"
                    board[board.index(chance1)]="X"
                    board2.remove(chance1)
                else:
                    print("invalid input")
                    co-=1
            display(displayboard)
            if len(board2)==0:
                print("You are pro! so game is draw...")
            else:
                print(board2)
                print("Hey you cheater! You are N O O B !")

elif chance=="O":
    games=[[8,3,[7,6,"v"],
             [4,6,"v"],
             [1,6,"v"],
             [2,6,"v"],
             [5,6,"v"],
             [6,1,[7,5,"v"],
                 [4,5,"v"],
                 [2,5,"v"],
                 [5,2,"v"]]],
         [7,1,[8,5,"v"],
             [4,5,"v"],
             [2,5,"v"],
             [3,5,"v"],
             [6,5,"v"],
             [5,3,[8,6,"v"],
                 [4,6,"v"],
                 [2,6,"v"],
                 [6,2,"v"]]],
         [4,3,[8,6,"v"],
             [7,6,"v"],
             [5,6,"v"],
             [1,6,"v"],
             [2,6,"v"],
             [6,7,[2,8,"v"],
                 [1,8,"v"],
                 [5,8,"v"],
                 [8,5,"v"]]],
         [1,3,[8,6,"v"],
             [7,6,"v"],
             [4,6,"v"],
             [5,6,"v"],
             [2,6,"v"],
             [6,7,[2,8,"v"],
                 [4,8,"v"],
                 [5,8,"v"],
                 [8,5,"v"]]],
         [2,3,[8,6,"v"],
             [7,6,"v"],
             [4,6,"v"],
             [5,6,"v"],
             [1,6,"v"],
             [6,7,[1,8,"v"],
                 [4,8,"v"],
                 [5,8,"v"],
                 [8,5,"v"]]],
         [3,1,[8,5,"v"],
             [7,5,"v"],
             [4,5,"v"],
             [2,5,"v"],
             [6,5,"v"],
             [5,7,[8,4,"v"],
                 [4,8,"v"],
                 [6,8,"v"],
                 [2,8,"v"]]],
         [6,7,[3,8,"v"],
             [2,8,"v"],
             [1,8,"v"],
             [4,8,"v"],
             [5,8,"v"],
             [8,1,[3,5,"v"],
                 [2,5,"v"],
                 [4,5,"v"],
                 [5,4,"v"]]],
         [5,1,[7,3,[8,6,"v"],
             [4,6,"v"],
             [2,6,"v"],
             [6,2,"v"]],
             [3,7,[6,4,"v"],
                 [2,8,"v"],
                 [4,8,"v"],
                 [8,4,"v"]],
             [8,2,[7,3,"v"],
                 [4,3,"v"],
                 [6,3,"v"],
                 [3,7,[6,4,"v"],
                     [4,6]]],
             [4,6,[8,3,"v"],
                 [7,3,"v"],
                 [2,3,"v"],
                 [3,7,[2,8,"v"],
                     [8,2]]],
             [2,8,[3,7,"v"],
                 [6,7,"v"],
                 [4,7,"v"],
                 [7,3,[4,6,"v"],
                     [6,4]]],
             [6,4,[3,7,"v"],
                 [2,7,"v"],
                 [8,7,"v"],
                 [7,3,[8,2,"v"],
                     [2,8]]]]]
    print("computer's Chance:")
     #co chance 1
    chance2=9
    com_board.add(chance2)
    displayboard[board.index(chance2)]="O"
    board[board.index(chance2)]="O"
    board2.remove(chance2)

    display(displayboard)

    #player 1
    for a in range(co):
        chance1=int(input("enter where you want to turn your 'O':"))
        if chance1 in  board:
            player_board.add(chance1)
            displayboard[board.index(chance1)]="X"
            board[board.index(chance1)]="X"
            board2.remove(chance1)
        else:
            print("invalid input")
            co-=1
    display(displayboard)

    #com chance 2
    print("computer's turn:")
    for a in games:
        if a[0]==chance1:
            chance2=a[1]
            com_board.add(chance2)
            displayboard[board.index(chance2)]="O"
            board[board.index(chance2)]="O"
            board2.remove(chance2)
            row=a
            row.pop(0)
            row.pop(0)

    display(displayboard)

    co=1
        #player chance 2
    for a in range(co):
        chance1=int(input("enter where you want to turn your 'X':"))
        if chance1 in  board:
            player_board.add(chance1)
            displayboard[board.index(chance1)]="X"
            board[board.index(chance1)]="X"
            board2.remove(chance1)
        else:
            print("invalid input")
            co-=1
    display(displayboard)

    #com chance 3
    print("computer's turn:")
    for a in row:
        if a[0]==chance1:
            chance2=a[1]
            com_board.add(chance2)
            displayboard[board.index(chance2)]="O"
            board[board.index(chance2)]="O"
            board2.remove(chance2)
            row=a
            row.pop(0)
            row.pop(0)

    display(displayboard)
    co=1
        #player chance 3
    for a in range(co):
        chance1=int(input("enter where you want to turn your 'X':"))
        if chance1 in  board:
            player_board.add(chance1)
            displayboard[board.index(chance1)]="X"
            board[board.index(chance1)]="X"
            board2.remove(chance1)
        else:
            print("invalid input")
            co-=1
    display(displayboard)

    #com chance 4
    print("computer's turn:")
    for a in row:
        if a[0]==chance1:
            chance2=a[1]
            com_board.add(chance2)
            displayboard[board.index(chance2)]="O"
            board[board.index(chance2)]="O"
            board2.remove(chance2)
            if len(a)==3:
                victory=True
            row=a
            row.pop(0)
            row.pop(0)
    display(displayboard)
    if victory==True:
        print("Oops! You  L O S E !")
    else:
        #player chance 4
        for a in range(co):
            chance1=int(input("enter where you want to turn your 'X':"))
            if chance1 in  board:
                player_board.add(chance1)
                displayboard[board.index(chance1)]="X"
                board[board.index(chance1)]="X"
                board2.remove(chance1)
            else:
                print("invalid input")
                co-=1
        display(displayboard)
        #com chance 5
        print("Computer's turn")
        for a in row:
            if a[0]==chance1:
                chance2=a[1]
                com_board.add(chance2)
                displayboard[board.index(chance2)]="O"
                board[board.index(chance2)]="O"
                board2.remove(chance2)
                if len(a)==3:
                    victory=True
                row=a
                row.pop(0)
                row.pop(0)
        display(displayboard)
        if victory==True:
            print("Oops! You  L O S E !")

else:
    print("Your keyboard is broken! T R Y   A G A I N !")