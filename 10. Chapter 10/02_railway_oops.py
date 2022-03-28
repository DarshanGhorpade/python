# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# oops concept using railway form example

# Create a class
class RailwayForm:
    formType = "RailwayForm"
    # Define a function
    def printData(self):
        print(f"Name: {self.name}")
        print(f"Train: {self.train}")

# Create an object of RailwayForm
darshansApplication = RailwayForm()

# Add my data to it
darshansApplication.name = "Darshan"
darshansApplication.train = "Rajdhani Express"

# Call printData()
darshansApplication.printData()