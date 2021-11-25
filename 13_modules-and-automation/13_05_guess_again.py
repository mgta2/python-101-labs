# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random

tries_left = 5
num = random.randint(1,10)

while tries_left > 0:
    guess = int(input("Guess a number from 1 to 9: "))
    if guess == num:
        print("Congratulations!")
        break
    tries_left -= 1
    print("You have", tries_left, "tries remaining.")