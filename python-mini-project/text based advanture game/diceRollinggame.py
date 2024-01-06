import random
diceRolling = True

while diceRolling:
    print(random.randint(1,6))
    playagain = input("Want to role again[y/n]")
    if playagain == "y":
        continue
    else:
        break