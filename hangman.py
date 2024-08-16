import random
import string
from words import words

#word file has words with hyphens and spaces but over 50k words, creating function to bypass them currently rather than sanitise the data, could use similar function to sanitise the data later.
def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) #all valid upper case letters
    used_letters = set() #letters that have been tried
    
    #I think there are 11 pieces?
    lives = 11
    
    #Letter Guessing
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and used the following letters: ", " ".join(used_letters))
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        
        guessed_letter = input("Guess a letter: ").upper()
        if guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
            else:
                lives = lives - 1
                print("Letter not in the word")
        
        elif guessed_letter in used_letters:
            print("You've already tried this letter, try again.")
            
        else:
            print("Invalid Character, try again")
        
    if lives == 00:
        print("You died, shame, the word was: ", word, ".")
    else:
        print("Congratulations, you guessed ", word, " correctly!")
hangman()