# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a python program to rename a file to “renamed_by_python.txt.”

import os

oldname = "rename.txt"
newname = "renamed_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    content = f.write(content)

os.remove(oldname)