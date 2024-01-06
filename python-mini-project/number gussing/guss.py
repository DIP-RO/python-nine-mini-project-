import random

RandomNumber = random.randrange(1,200)
userInput = int(input("Guess Number:"))
if userInput>RandomNumber:
    print(RandomNumber)
    print("number is high")
elif RandomNumber>userInput:
    print(RandomNumber)
    print("number low")
elif RandomNumber == userInput:
    print(RandomNumber)
    print("match.congratulation")
else:
    print(RandomNumber)
    print("canot found .input valid number")