import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    '''
    print the game state and the secret word
    '''

    print(STAGES[mistakes])
    display_word = ""
    for char in secret_word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_again():
    '''
    Asks the user if they would like to play again.
    Returns True to play again, False to end the game.
    '''
    while True:
        print("\nDo you want play again")
        user_input = input("(Y/N)").lower().strip()

        if user_input == "y":
            return True
        elif user_input == "n":
            print("\nThank you for playing, Bye!")
            return False
        else:
            print("\nEnter only Y or N ")

def play_game():
    '''
    Retrieves the user's input of letters.
    Checks for incorrect attempts and determines whether the attempt is correct.
    Loops until the user chooses not to play again.
    '''
    print("Welcome to Snowman Meltdown!")

    while True:
        secret_word = get_random_word()
        mistakes = 0
        guessed_letters = []
        game_over = False

        while not game_over:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = input("Guess a letter: ").lower().strip()

            if guess.isalpha() and len(guess) == 1:
                if guess in secret_word:
                    guessed_letters.append(guess)
                else:
                    mistakes += 1
                    if mistakes == len(STAGES):
                        print("""\n     ~~~~~~~\n    ~~~~~~~~""")
                        print("\nGame Over! The snowman has melted")
                        print(f"The word was: {secret_word}")
                        game_over = True

                if not game_over and all(char in guessed_letters for char in secret_word):
                    print(f"\n{secret_word}, correct")
                    print("Congratulations, you saved the snowman!")
                    game_over = True

                if not game_over:
                    print("You guessed:", guess)
            else:
                print("\nPlease enter just ONE ALPHABETICAL letter!")

        if not play_again():
            break

