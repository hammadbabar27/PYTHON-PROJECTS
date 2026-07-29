#Random Number Guess From 1 to 100 

print(" Welcome To Number Guess Game \n")

import random

target = random.randint(1,100)


while True:
    guess = input("Guess the Number or Hint or Quit: ")

    if (guess.lower() == "quit"):
       break

    if (guess.lower() == "hint"):
        if(target %2 == 0):
           print("\nNumber is EVEN\n")
           continue

        else:
           print("\nNumber is ODD\n")
           continue

    try:
     guess = int(guess)
    except ValueError:
     print("Please enter a number, 'hint', or 'quit'")
     continue

    if(guess > 0 and guess <101):    

        if (guess == target):
          print("You Guess the Correct Number i.e.", guess)
          break

        elif(guess > target):
          print("The Number You Guess is Greater Than the Target\n Try Again")

        elif(guess < target):
          print("The Number You Guess is Less Than the Target\n Try Again")


    else:
       print("Number Shuold be Between 1 to 100 inclusive")

print(" ---GAME OVER--- ")