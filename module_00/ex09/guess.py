from random import randint


class RangeError(Exception):
    pass


print(
    "This is an interactive guessing game!\n"
    "You have to enter a number between 1 and 99 "
    "to find out the secret number.\n"
    "Type 'exit' to end the game.\n"
    "Good luck!\n"
)

secret_number = randint(1, 99)
guess = 0
attempts = 0

while guess != secret_number:
    attempts += 1
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess == "exit":
        print("Goodbye!")
        exit()
    try:
        guess = int(guess)
        if guess not in range(1, 100):
            raise RangeError
    except ValueError:
        print("That's not a number.")
        continue
    except RangeError:
        print("That's not a number between 1 and 99.")
        continue
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
print("Congratulations, you've got it!")
print("The secret number was", secret_number)
print(f"You won in {attempts} attempts!")
