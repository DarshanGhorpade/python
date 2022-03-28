# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# Place these files in a folder for a 13- year old boy.

for i in range(2, 21):  # i will take values from 2 to 20
    with open(f"tables/Multiplication_table_of_{i}.txt", "w") as f:
        for j in range(1, 11):      # j will take values from 1 to 10
            f.write(f"{i} X {j} = {i*j}\n")     # escape sequence character
            if j!=10:
                f.write('\n')