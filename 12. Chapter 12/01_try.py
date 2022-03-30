# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# Exception Handling in Python
# There are many built-in exceptions that are raised in Python when something goes wrong.
# Exceptions in Python can be handled using a try statement. The code that handles the exception is written in except clause.


while(True):
    print("Press q to exit")
    a = input("Enter a number: ")

    if a == 'q':
        break

    try:
        print("Trying....")
        a = int(a)

        if a > 6:
            print("You entered number greater than 6.")
    except Exception as e:
        print(f"Your input resulted in an error {e}")

print("Thanks for playing the game.")