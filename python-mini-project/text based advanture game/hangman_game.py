word ="Dipro"
chance = 5
guess = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guess:
            print(letter, end ="")
        else:
            print("_",end = "")
    x = input(f"your changes is {chance}, guss the letter:")
    guess.append(x.lower())
    if x.lower() not in word.lower():
        chance -= 1
        if chance == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guess:
            done =False 

if done:
    print(f"yes,you win {word}")
else:
    print("you loose")