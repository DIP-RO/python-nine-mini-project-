answer = input("do u want to play this game?[yes/no]")
if answer == 'yes':
    print("welcome")
    answer = input("jungle or cave?")
    if answer == "jungle":
        print("tiger ear")
    elif answer == "cave":
        print("bear in cave")
        answer = input("fight bear?")
        if answer == "fight":
            print("you lose")
        else:
            print("win")
    
else:
    print("please play this game at least 1 time")
