# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to find out whether a given post is talking about "Darshan" or not.

post = input("Enter post\n")
post = post.lower()

if "darshan" in post:
    print("Post is talking about Darshan")
else:
    print("Post is not talking about Darshan")