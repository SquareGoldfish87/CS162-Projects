""" Project 1 Complex Object; House
This program will help the user find common items in a house.

Vincent Lopez

Design:

Use while conditions to ask user what the following command is. If quitting the code is asked, it should allow the user to quit at any moment.

Using classes, methods, and variables ask for the user where in the program they would like to look into.

Use some testing to allow for a more user-friendly terminal.


I attempted to add a shebang, but it caused it to fail...


Testing would be conditions that asks and excepts errors or fatal fails; Before the user is given the error over the terminal. Testing will provide a much more streamlined and quicker response for the user.
"""
# This program edited by Jake Lester. Anything hashed out is my comments.
# The idea behind the new file opening functionality is to allow a user to bypass the user input sections of the program and instead
# execute selections written in a seperate file.

# First, we define the 'house' class. It works out easier to do it early.
class house:
    """A class that represents a house"""

    def __init__(self):
        """Creates containers"""
        self.livingroom = "Television, Couches, Pets, Family, and Friends are usually found in the living room!\n"
        self.Kitchen = "Range, Microwave, Toaster, Coffee makers, and Delicious Goodies of all kinds are made here!\n"
        self.Garage = "Hmmm... In the Garage there is usually washing and drying machines, furnace, and if there is space, maybe even a car!\n"
        self.Bedroom = "This is where users usually go to rest, a bed, desk, and whatever makes the user happy or relaxed. Whether that be connected online or disconnected.\n"

    def get_livingroom(self):
        """Pull livingroom info."""
        return self.livingroom

    def get_Kitchen(self):
        """Pull Kitchen info."""
        return self.Kitchen

    def get_Garage(self):
        """Pull Garage info."""
        return self.Garage

    def get_Bedroom(self):
        """Pull Bedroom info."""
        return self.Bedroom

# We're going to slightly alter the original code in order to add the option for the user to pass their own file in.
print(f"Hello! I am here to help find categories in a house\n")
usr_question = (
    input("If you would like to continue please press Y for yes, N for No, or F to read a file: \n")
).lower()

if usr_question == "n":
    print("Sorry I could not help you, have a great day!\n")
    quit()

# Here we're going to resolve the file opening. Assuming the file is formatted properly, this should read their file line by line
# and go to the room specified in each line.
if usr_question == "f":
    usr_file = input("Enter the name of the file you would like to use: ")
    try:
        with open(usr_file, "r") as f:
            for line in f:
                usr_room = f.readline()
                usr_room = usr_room.strip()

                my_house = house()

                if usr_room == "livingroom":
                    print(
                        f"You have decided to look at the livingroom\n\n {my_house.get_livingroom()}")
                elif usr_room == "kitchen":
                    print(
                        f"You have decided to look at the Kitchen\n\n {my_house.get_Kitchen()}")
                elif usr_room == "garage":
                    print(
                        f"You have decided to look at the Garage\n\n{my_house.get_Garage()}")
                elif usr_room == "bedroom":
                    print(
                        f"You have decided to look at the Bedroom\n\n {my_house.get_Bedroom()}")
                elif usr_room == "q":
                    print("Have a good one! Goodbye!")
                    quit()
                else:
                    print("Here be dragons! Go back my friend!\n\n")
                    pass
                
    except FileNotFoundError:
        print("File not found. Please try again.")
        

while True:
    if usr_question == "y":
        print(f"Welcome, I will help you find different secctions to a house!\n")
        print("Which parts of the house would you like to explore? I can give you the jist the rooms I know. \n")
        usr_room = input(
            "The rooms I know: Livingroom, Kitchen, Garage, or Bedroom\n\nWhich would you like to explore?\n\nPlease use whole words, or ENTER Q to quit:\n").lower()

    class house:
        """A class that represents a house"""

        def __init__(self):
            """Creates containers"""
            self.livingroom = "Television, Couches, Pets, Family, and Friends are usually found in the living room!\n"
            self.Kitchen = "Range, Microwave, Toaster, Coffee makers, and Delicious Goodies of all kinds are made here!\n"
            self.Garage = "Hmmm... In the Garage there is usually washing and drying machines, furnace, and if there is space, maybe even a car!\n"
            self.Bedroom = "This is where users usually go to rest, a bed, desk, and whatever makes the user happy or relaxed. Whether that be connected online or disconnected.\n"

        def get_livingroom(self):
            """Pull livingroom info."""
            return self.livingroom

        def get_Kitchen(self):
            """Pull Kitchen info."""
            return self.Kitchen

        def get_Garage(self):
            """Pull Garage info."""
            return self.Garage

        def get_Bedroom(self):
            """Pull Bedroom info."""
            return self.Bedroom

    my_house = house()

    if usr_room == "livingroom":
        print(
            f"You have decided to look at the livingroom\n\n {my_house.get_livingroom()}")
    elif usr_room == "kitchen":
        print(
            f"You have decided to look at the Kitchen\n\n {my_house.get_Kitchen()}")
    elif usr_room == "garage":
        print(
            f"You have decided to look at the Garage\n\n{my_house.get_Garage()}")
    elif usr_room == "bedroom":
        print(
            f"You have decided to look at the Bedroom\n\n {my_house.get_Bedroom()}")
    elif usr_room == "q":
        print("Have a good one! Goodbye!")
        quit()
    else:
        print("Here be dragons! Go back my friend!\n\n")
    pass
quit()
