# Hangman Game Project

# Pick a random word from the given list:
import random
list = ["hangman", "fountain", "astronaut", "trigonometry"]
rand_index = random.randrange(0,len(list))
word = list[rand_index]
length = len(word)

print("You must guess the word. You lose after 5 mistakes.")

mistakes = 0
current = ""
for i in range(0,length):
    current += "_ "

correct_letters = ""

while mistakes < 5:
    print(current)
    guess = input("Guess a letter: ")
    if len(guess) != 1:
        print("Invalid entry.")
        continue
    elif not(guess.isalpha()):
        print("Invalid entry.")
        continue
    guess = guess.lower()
    
    if guess in word:
        correct_letters += guess
        
        # Now define the new 'current'
        current = ""
        done = True
        for i in range(0,length):
            if word[i] in correct_letters:
                current += (word[i] + " ")
            else:
                current += "_ "
                done = False
        if done == True:
            print("Congratulations! The word was:", word)
            break
        
    else:
        mistakes += 1
        print(guess, "is not in the word.")
        print(f"You have made {mistakes} mistakes.")
if mistakes == 5:
    print("You lost :(")