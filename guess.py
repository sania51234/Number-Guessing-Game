import random

def get_random_number(level):
    """Generate a random number based on the difficulty level."""
    if level == 'easy':
        return random.randint(1, 10)
    elif level == 'medium':
        return random.randint(1, 50)
    elif level == 'hard':
        return random.randint(1, 100)

def choose_difficulty():
    """Let the user select a difficulty level."""
    print("Choose difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game():
    """Main game logic."""
    difficulty = choose_difficulty()
    number = get_random_number(difficulty)
    guess_count = 0
    guessed_number = None

    print(f"\nI've picked a number based on {difficulty} difficulty. Start guessing!\n")

    while guessed_number != number:
        try:
            guessed_number = int(input("Enter your guess: "))
            guess_count += 1

            if guessed_number < number:
                print("Go higher!")
            elif guessed_number > number:
                print("Go lower!")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nCongratulations! You guessed the number {number} in {guess_count} guesses.")

    return guess_count

def main():
    """Main loop for starting the game and keeping track of high scores."""
    print("Welcome to the Number Guessing Game!")
    
    high_score = None

    while True:
        guess_count = play_game()

        if high_score is None or guess_count < high_score:
            high_score = guess_count
            print(f"New high score: {high_score} guesses!")
        else:
            print(f"Your best score is {high_score} guesses.")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
