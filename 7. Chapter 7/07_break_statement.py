# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# for loop with break statement
# ‘break’ is used to come out of the loop when encountered. It instructs the program to – Exit the loop now.

for i in range(10):
    print(i)
    if i == 5:  # This will print 0, 1, 2, 3, 4 and 5
        break
else:
    print("This is inside else of for") # This is printed when the loop exhausts!