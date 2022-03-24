# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# for loop with continue statement
# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the program to “skip this iteration.”

for i in range(10):
    if i == 5:  # if i is 5, the iteration is skipped
        continue
    print(i)