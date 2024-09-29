import random

def play_game():
    # Generating a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game")
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Start  loop
    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the game
def main():
    play_again = "y"
    while play_again.lower() == "y":
        play_game()
        play_again = input("Do you want to play again? (y/n): ")

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
