def clear_screen():
    print("\n" * 50)

def play_game():
    clear_screen()
    print("=== Number Guessing Game ===\n")
    print("I have picked a number between 1 and 100.")
    print("Can you guess it?\n")

    import random   # Only importing random here (very common for games)
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue

            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!")
                if attempts <= 5:
                    print("Excellent! You're a guessing master!")
                elif attempts <= 8:
                    print("Good job!")
                else:
                    print("Nice, you got it!")
                return True

            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"\nGame Over! The number was {secret_number}.")
    return False

def main():
    print("Welcome to the Number Guessing Game!\n")
    
    while True:
        play_game()
        
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()