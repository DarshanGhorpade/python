# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a class Train which has methods to book a ticket, get status(no of seats), 
#   and get fare information of trains running under Indian Railways.

class Train:

    # constructor
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("\n******************************************\n")
        print(f"Name of Train: {self.name}")
        print(f"Seats available: {self.seats}")
        print("\n******************************************\n")

    def getFareInfo(self):
        print(f"Price of the tickets: ₹ {self.fare}")

    def bookTickets(self):
        if self.seats>0:
            print(f"Your ticket has been booked. Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal.")

    def cancelTicket(self):
        pass

intercity = Train("Intercity Express: 14015", 100, 2)
intercity.getStatus()
intercity.getFareInfo()

intercity.bookTickets()
intercity.bookTickets()
intercity.bookTickets()

intercity.getStatus()