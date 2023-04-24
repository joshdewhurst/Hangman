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

    while guesses_left > 0 and guess != word:
        print("Guess the word: " + guess)
        print("Guesses left: " + str(guesses_left))
        print("Letters guessed: " + str(letters_guessed))
        letter = input("Guess a letter: ").lower()

        if letter in letters_guessed:
            print("You already guessed that letter. Try again.")
        elif letter in word:
            print("Correct!")
            guess = update_word(word, guess, letter)
        else:
            print("Wrong!")
            guesses_left -= 1

        letters_guessed.append(letter)

    if guess == word:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost. The word was " + word + ".")

    play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

# Start the game
hangman()
