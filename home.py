#game mode
a=int(input("Choose the game mode:\n1. Single Player\n2. Multi Player\nEnter option you choose:"))


#game mode pvp
if (a==2):
    import pvp

#gamemode pvc
elif (a==1):
    d=int(input("\nchoose the deficulti:\n1.Easy\n2.Medium\n3.Hard(impossible)\nEnter option you choose:"))
    if d==1:
        import epvc
    elif d==2:
        import mpvc
    elif d==3:
        import hpvc
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
