# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to find out whether a student is pass or fail, if ot requires total 40% and atleast 33% in each subject to pass.
# Assume 3 subjects and take marks as input from the user.

sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))

if sub1<33 or sub2<33 or sub3<33:
    print("You are fail because you have less than 33% in one or more subjects")

elif (sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40%")

else:
    print("Congratulations! You passed the exams")