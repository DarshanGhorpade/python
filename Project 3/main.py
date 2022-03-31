# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Project 3: Student Library
# Implement a student library system using OOPs where students can borrow a book from the list of books.
# Create a separate Library and Student class.
# Your program must be menu-driven.
# You are free to choose the methods and attributes of your choice to implement this functionality.

# Create a class Library
class Library:

    # constructor
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books in this Library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else.\nPlease wait until the book is available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


# Create a class Student
class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return: ")
        return self.book


if __name__ == "__main__":
    # Create object of Library and pass list of book names
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python", "Data structures"])
    # Create object of Student
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ====== Welcome To Central Library ======
        Please choose an option
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''

        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")