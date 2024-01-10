# Imports
import random

# Creating a List of Fruits
word_list = ['apple', 'banana', 'orange', 'grape']

print("Word List:", word_list)

# Assigning a randomly selected word from the list to a variable called "word"
word = random.choice(word_list)

# Print the randomly selected word 
print("Randomly selected word:", word)

while True:
    # Taking user input
    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break  
    else:
        print("Oops! That is not a valid input.")

# Continue with the rest of your code to check if the guessed letter is in the word.
if len(guess) == 1 and guess.isalpha():
    if guess in word:
        print("The guess is correct! The letter '{}' is in the word.".format(guess))
    else:
        print("The guess is incorrect. The letter '{}' is not in the word.".format(guess))
else:
    print("Invalid input. Please enter a single letter.")
