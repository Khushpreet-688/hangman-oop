"""
ACIT2515 Lab

Week 3
OOP-Hangman

"""
import random

class SecretWord:
    """
    SecretWord class contains various methods that can be used on a word(obj.) that may be random or given by the user.
        show_letters(): calls the function show_letters_in_word() to print matching letters
        check_letters(): returns TRUE or FALSE based on whether the entire letters list matching letters in the word
        check(): instead of a list of letters, it compares the secret word to a word (string) provided by the user
    """
    def __init__(self, secret_word = None):
        if (secret_word == None):
            self._secret_word = pick_random_word()
        else:
            self._secret_word = secret_word.upper()
    def show_letters(self, list_letters):
        return show_letters_in_word(self._secret_word, list_letters)
    def check_letters(self, list_letters):
        return all_letters_found(self._secret_word, list_letters)
    def check(self, str):
        if (str.upper() == self._secret_word.upper()):
            return True
        else:
            return False


class Game:
    """
    Game class is used to create an object which could be called with play() method to play the game
    while constructing an object, number of turns should be passed as argument to the class, however, the 
    word_given argument is optional, it can be used to pass in a secret word to play the game instead of asking the 
    program to choose a random word.
    """
    def __init__(self, turns, word_given = None):
        self.word = SecretWord(word_given)
        self.turns_remaining = turns
        self.letters = []

    def play_one_round(self):
        user_input = input("Please Enter a letter: ").upper()
        while (user_input in self.letters):
            user_input = input("Please enter another letter: ").upper()
        self.letters.append(user_input)
        print(self.word.show_letters(self.letters))
        if(self.word.check_letters(self.letters)):
            return True
        else:
            return False

    def play(self):
        valid = True
        while valid:
            if (self.turns_remaining == 0):
                print(f"You lost!! The word was {self.word._secret_word}")
                valid = False
            else:
                print(self.word.show_letters(self.letters))
                result = self.play_one_round()
                self.turns_remaining -= 1
                print(f'Number of tries left = {self.turns_remaining}')
                if (result):
                    print("You guessed the correct word! You Won!!")
                    valid = False



def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    with open("words.txt", "r") as f:
        words_string  = f.read()
        words_list = words_string.split()
    selected_word = random.choice(words_list)
    return selected_word

def show_letters_in_word(word, letters):
    """
    First, make sure word is uppercase, and all letters are uppercase.
    This function scans the word letter by letter.
    If the letter of the word is in the list of letters, display it.
    Otherwise, display an underscore (_).

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
   
    my_string = ""
    
    for letter in word.upper():
        if (letter in letters):
            my_string += letter
        else:
            my_string += '_'
        my_string += ' '
    return my_string.strip()

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    for letter in word.upper():
        if (letter not in letters):
            return False
    return True

def main():
    my_game = Game(10)
    my_game.play()

if __name__ == "__main__":
    main()