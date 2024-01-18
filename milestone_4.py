import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def get_word_guessed(self):
        return ''.join(self.word_guessed)

    def is_word_guessed(self):
        return '_' not in self.word_guessed

    def make_guess(self, letter):
        if letter in self.list_of_guesses:
            return "You've already guessed this letter."

        self.list_of_guesses.append(letter)
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
            return "Good guess!"
        else:
            self.num_lives -= 1
            return "Wrong guess. You have {} lives left.".format(self.num_lives)

    def play_game(self):
        print("Welcome to Hangman!")
        while self.num_lives > 0 and not self.is_word_guessed():
            print("Word: ", self.get_word_guessed())
            print("Guessed Letters: ", ', '.join(self.list_of_guesses))
            guess = input("Guess a letter: ").lower()
            result = self.make_guess(guess)
            print(result)

        if self.is_word_guessed():
            print("Congratulations! You've guessed the word:", self.word)
        else:
            print("Game over. The word was:", self.word)


word_list = ['apple', 'banana', 'orange', 'grape']
game = Hangman(word_list)
game.play_game()
