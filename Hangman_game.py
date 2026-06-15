"""
Text-Based Hangman Game
-----------------------
Features:
1. Uses a predefined list of words
2. Randomly selects a word each game
3. Displays hidden word with underscores
4. Allows only 6 incorrect guesses
5. Shows all guessed letters
6. Validates user input
7. Uses while loops, if-else, lists, and strings
8. Displays ASCII-art hangman
9. Allows the player to play again
10. Beginner-friendly and follows good coding practices
"""

import random

# Maximum number of incorrect guesses allowed
MAX_WRONG_GUESSES = 6

# Predefined list of words (Programming Theme)
WORD_LIST = [
    "python",
    "variable",
    "function",
    "loop",
    "compiler",
    "string",
    "integer"
]

def choose_word():
    """
    Randomly select and return a word from the list.
    """
    return random.choice(WORD_LIST)


def display_game_state(secret_word, guessed_letters, wrong_guesses):
   
   

    # Display the hidden word
    displayed_word = []

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word.append(letter)
        else:
            displayed_word.append("_")

    print("Word: ", " ".join(displayed_word))

    # Display guessed letters
    if guessed_letters:
        print("Guessed Letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed Letters: None")

    # Display remaining attempts
    print("Remaining Attempts:", MAX_WRONG_GUESSES - wrong_guesses)


def get_player_guess(guessed_letters):
    """
    Get and validate user input.
    """
    while True:
        guess = input("\nEnter a letter: ").lower().strip()

        # Check for single character
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        # Check if input is alphabetic
        if not guess.isalpha():
            print("Only alphabet letters are allowed.")
            continue

        # Check for repeated guess
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        return guess


def check_win(secret_word, guessed_letters):
    """
    Check if the player has guessed the entire word.
    """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():
    """
    Main game logic.
    """
    secret_word = choose_word()

    guessed_letters = []
    wrong_guesses = 0

    # Main game loop
    while wrong_guesses < MAX_WRONG_GUESSES:

        display_game_state(
            secret_word,
            guessed_letters,
            wrong_guesses
        )

        guess = get_player_guess(guessed_letters)

        # Store guessed letter
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print("Good job! That letter is in the word.")

            # Check for win
            if check_win(secret_word, guessed_letters):
                display_game_state(
                    secret_word,
                    guessed_letters,
                    wrong_guesses
                )

                print("\nCongratulations! You guessed the word!")
                print("The word was:", secret_word)
                return

        else:
            wrong_guesses += 1
            print("Wrong guess!")

    # Player loses
    display_game_state(
        secret_word,
        guessed_letters,
        wrong_guesses
    )

    print("\nGame Over!")
    print("You ran out of attempts.")
    print("The correct word was:", secret_word)


def main():
    """
    Program entry point.
    Controls replay option.
    """
    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME ")
    print("=" * 40)

    while True:
        play_game()

        play_again = input(
            "\nDo you want to play again? (y/n): "
        ).lower().strip()

        if play_again != "y":
            print("\nThank you for playing Hangman Game!")
            break


# Start the program
if __name__ == "__main__":
    main()