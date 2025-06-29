import random

print("🎲 Welcome to the Number Guessing Game!")
print("--------------------------------------")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize guess
guess = None
attempts = 0

while guess != secret_number:
    try:
        guess = int(input("🔢 Enter your guess (1-100): "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
    except ValueError:
        print("⚠ Please enter a valid number.")