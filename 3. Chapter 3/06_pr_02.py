# Author: Darshan Ghorpade
# Location: Earth
# Date: 22/03/2022

# Q. Write a program to fill in a letter template given with name and date.

# letter = '''Dear <|Name|>,
#               you are selected!
#               <|Date|>'''

letter = '''Dear <|Name|>,
Greetings from ABC coding house. I am happy to tell you about your selection.
you are selected!
Have a great day ahead!
Thanks and regards,
Bill
<|Date|>'''

name = input("Enter your name: ")
date = input("Enter date: ")

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)