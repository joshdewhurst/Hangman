import random

# List of words for the game
words = ['python', 'programming', 'computer', 'data', 'science', 'california', 'april', 'software']

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to update the word with correctly guessed letters
def update_word(word, guess, letter):
    for i in range(len(word)):
        if word[i] == letter:
            guess = guess[:i] + letter + guess[i+1:]
    return guess

# Main game loop
def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guess = "_" * len(word)
    guesses_left = 6
    letters_guessed = []
