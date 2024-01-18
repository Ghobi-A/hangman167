import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.
        :param word_list: List of words for the game.
        :param num_lives: Number of lives a player starts with.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def get_word_guessed(self):
        """
        Get the current state of the word being guessed.
        :return: String representing the word guessed so far.
        """
        return ''.join(self.word_guessed)

    def is_word_guessed(self):
        """
        Check if the word has been completely guessed.
        :return: Boolean indicating if the word has been guessed.
        """
        return '_' not in self.word_guessed

    def make_guess(self, letter):
        """
        Make a guess in the game.
        :param letter: The guessed letter.
        :return: String indicating the result of the guess.
        """
        if letter in self.list_of_guesses:
            return "You've already guessed this letter."

        self.list_of_guesses.append(letter)
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
                    self.num_letters -= 1
            return "Good guess!"
        else:
            self.num_lives -= 1
            return "Wrong guess. You have {} lives left.".format(self.num_lives)

def play_game(word_list):
    """
    Play a game of Hangman.
    :param word_list: List of words to use in the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if num_lives == 0:
            print('You lost! The word was:', game.word)
            break

        if game.is_word_guessed():
            print('Congratulations. You won the game! The word was:', game.word)
            break

        print("Word: ", game.get_word_guessed())
        print("Guessed Letters: ", ', '.join(game.list_of_guesses))
        guess = input("Guess a letter: ").lower()
        result = game.make_guess(guess)
        print(result)

# Word list
word_list = ['apple', 'banana', 'orange', 'grape']

# Play the game
play_game(word_list)