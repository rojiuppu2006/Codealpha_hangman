import random

# -------------------- GAME SETTINGS --------------------

WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "algorithm",
    "database",
    "robotics",
    "software",
    "machine",
    "learning",
    "artificial",
    "intelligence",
    "keyboard",
    "variable",
    "function"
]

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]


# -------------------- DISPLAY FUNCTIONS --------------------

def display_header():
    """Display the game title."""

    print("\n" + "=" * 45)
    print("              HANGMAN GAME")
    print("=" * 45)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect attempts allowed.")


def display_game(word, guessed_letters, wrong_attempts):
    """Display the Hangman drawing and current word."""

    print(HANGMAN_STAGES[wrong_attempts])

    displayed_word = [
        letter if letter in guessed_letters else "_"
        for letter in word
    ]

    print("Word:", " ".join(displayed_word))
    print(f"Wrong attempts remaining: {MAX_ATTEMPTS - wrong_attempts}")

    if guessed_letters:
        print(
            "Guessed letters:",
            " ".join(sorted(guessed_letters))
        )

    return "_" not in displayed_word


# -------------------- INPUT VALIDATION --------------------

def get_guess(guessed_letters):
    """Get one valid, previously unguessed letter."""

    while True:
        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter exactly one alphabetic letter.")

        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")

        else:
            return guess


def ask_play_again():
    """Ask whether the player wants another round."""

    while True:
        choice = input("\nWould you like to play again? (yes/no): ")
        choice = choice.strip().lower()

        if choice in ("yes", "y"):
            return True

        if choice in ("no", "n"):
            return False

        print("Invalid choice! Please enter yes or no.")


# -------------------- GAME LOGIC --------------------

def play_game():
    """Run one complete round and return whether the player won."""

    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_attempts = 0

    display_header()

    while wrong_attempts < MAX_ATTEMPTS:

        won = display_game(
            word,
            guessed_letters,
            wrong_attempts
        )

        if won:
            print("\nCongratulations! You guessed the word!")
            print("The hidden word was:", word)
            return True

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess! The letter is in the word.")
        else:
            wrong_attempts += 1
            print("Wrong guess! One attempt has been used.")

    # Show the final drawing and reveal the word after losing.
    display_game(word, guessed_letters, wrong_attempts)

    print("\nGAME OVER! You have used all your attempts.")
    print("The correct word was:", word)

    return False


# -------------------- MAIN PROGRAM --------------------

def main():
    """Manage multiple rounds and maintain the score."""

    wins = 0
    losses = 0

    print("Welcome to the Python Hangman Game!")

    while True:

        result = play_game()

        if result:
            wins += 1
        else:
            losses += 1

        print("\n" + "-" * 45)
        print("                 SCOREBOARD")
        print("-" * 45)
        print("Games played:", wins + losses)
        print("Wins:", wins)
        print("Losses:", losses)
        print("-" * 45)

        if not ask_play_again():
            break

    print("\nThank you for playing Hangman!")
    print(f"Final score: {wins} win(s), {losses} loss(es).")
    print("See you next time!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame stopped. Thanks for playing!")
