# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# if __name__==’__main__’ in Python
# __name__ evaluates to the name of the module in Python from where the program is ran.
# If the module is being run directly from the command line, the __name__ is set to string “__main__”.
# Thus this behavior is used to check whether the module is run directly or imported to another file.

def greet(name):
    print(f"Good morning, {name}")

# print(__name__)   # will print __main__

if __name__ == '__main__':
    n = input("Enter a name: ")
    greet(n)