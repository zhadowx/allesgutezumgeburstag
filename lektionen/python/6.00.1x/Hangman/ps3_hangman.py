# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist:list) -> str:
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord:str, lettersGuessed:list) -> bool:
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    boolist= []
    for l in secretWord:
        boolist.append(l in lettersGuessed)

    for e in boolist:
        if e != True:
            return False
            
    return True



def getGuessedWord(secretWord: str, lettersGuessed:list) -> str:
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    gword = ""
    for l in secretWord:
        if l in lettersGuessed:
            gword+=l
        else:
            gword+="_ "
    return gword 


def getAvailableLetters(lettersGuessed: list) -> str:
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avlet = "abcdefghijklmnopqrstuvwxyz"
    for l in lettersGuessed:
        avlet = avlet.replace(l, "")
    return avlet    


def hangman(secretWord:str):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    number_of_guesses = 8
    lettersGuessed = ""

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")

    while number_of_guesses > 0 and not isWordGuessed(secretWord, lettersGuessed):

        print("You have " + str(number_of_guesses) + " guesses left")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        letterGuessed = input("Please guess a letter: ").lower()
        if letterGuessed in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
        else:
            lettersGuessed+=letterGuessed
            if letterGuessed in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                number_of_guesses-= 1

    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(loadWords()).lower()
hangman(secretWord)









