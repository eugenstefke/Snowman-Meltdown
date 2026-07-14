import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
ALPHABETICAL_LETTERS = "abcdefghijklmnopqrstuvwxyz"
ONLY_ONE_CHAR = 1

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

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
    asks the user if they would like to play again, restarts the game or ends the game
    '''
    while True:
        print("\nDo you want play again")
        user_input = input("(Y/N)").lower().strip()

        if user_input == "y":
            play_game()
        elif user_input == "n":
            print("\nThank you for playing, Bye!")
            raise SystemExit
        else:
            print("\nEnter only Y or N ")

def play_game():
    '''
    Retrieves the user’s input of letters.
    Checks for incorrect attempts and determines whether the attempt is correct.
    Calls the ‘play again’ function.
    '''
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower().strip()

        if guess in ALPHABETICAL_LETTERS and len(guess) == ONLY_ONE_CHAR:
            if guess in secret_word:
                guessed_letters.append(guess)

            if guess not in secret_word:
                mistakes += 1
                if mistakes == len(STAGES):
                    print("""\n     ~~~~~~~\n    ~~~~~~~~""")
                    print("\nGame Over! The snowman has melted")
                    print(f"The word was: {secret_word}")
                    play_again()

            if all(char in guessed_letters for char in secret_word):
                print(f"\n{secret_word}, correct")
                print("Congratulations, you saved the snowman!")
                play_again()
        else:
            print("\nPlease enter just ONE ALPHABETICAL letter!")

        print("You guessed:", guess)


if __name__ == "__main__":
    play_game()