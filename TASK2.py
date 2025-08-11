import random

print("Welcome to Codmetric Number Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess it?\n")

# Generate random number
secret_number = random.randint(1, 100)

# Counter for attempts
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.\n")
