#  Author: Darshan Ghorpade
#  Location: Earth
#  Date: 21/03/2022

# Q. Install an external module and use it to perform an operation of your interest

# Here we install playsound module
# by using command
# pip install playsound


# import external module
from playsound import playsound

# to use this module give path of mp3 file to it
# playsound('audio.mp3')

# here we have to use double back slash \ 
# since if we put single character after single back slash \ it is supposed as escape sequence character
playsound('D:\\python\\1. Chapter 1\\audio.mp3')