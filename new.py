import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Variable to track the number of attempts
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_the_number()  # Restart the game
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    guess_the_number()
