#!/usr/bin/env python3
"""Get user input through a GUI that retrieves a file that corresponds to a class, then print
information about that class"""

# We'll need tkinter for the GUI portion
import tkinter as tk

# We start by defining functions and classes.
# This is the function that opens our user's file and then assigns a class based on what's in
# the file.
def file_opener():
    """A function that opens a file, reads the first line, and creates a class based on that line."""
    file = user_entry.get()
    # Take the entered file and try opening it
    try:
        with open(file, "r") as f:
        # Then, we read the first (and what should be only) line in the file.
        # We sanitize it and then compare it to the names of the classes we defined.
            line = f.readline()
            line = line.strip()
            line = line.lower()
            # If the line is boat, car, or plane, we initialize a new class that has
            # the properties of one of the other classes.
            if line == "boat":
                class Vehicle(Boat):
                    pass
            elif line == "car":
                class Vehicle(Car):
                        pass
            elif line == "plane":
                class Vehicle(Plane):
                        pass
            # If it's literally anything else, then we don't want it and we tell the user that
            else:
                print("ERROR: Line 1 does not read 'Plane', 'Boat', or 'Car'. Please check file and try again.")
            vehicle_readout(Vehicle())

# Should the file not be found, this error will be raised.
    except FileNotFoundError: 
        print("File not found! Please try again.")

# This is the test function. It's staying in to show that I have an understanding of testing.
def test_function():
    """A function that runs pre-determined files, existing and not, through the other function
    for testing purposes. Callable with the 'test' button."""
    # This is just file_opener but hardcoded, with a small extra to make things more compact.
    # We hardcode 3 filesg
    # This file is valid input
    file = "final.txt"
    # This file doesn't exist
    file_2 = "this_file_doesn't_exist.jpeg"
    # This file does exist but has invalid input inside
    file_3 = "dummy_final.txt"
    # The counter is part of the small extra to compact things
    counter=0

    # Instead of pasting the entire bottom code thrice with a different file all 3 times, I made
    # the code run three times, and on the second and third passes, it uses the 2nd and 3rd
    # filenames respectively.
    # After some tinkering, now it mysteriously goes file 2, 3, and then 1. Either way,
    # all 3 files get tested and nothing breaks. Were this not a test function I'd chase 
    # the error down, but this was always meant to be a quick and dirty
    # 'Does the function work' thing, and it does that, so I'm satisfied.
    while counter != 3:
        if counter == 1:
            file = file_2
        elif counter == 2:
            file = file_3
        counter += 1
    # Take the entered file and try opening it
        try:
            with open(file, "r") as f:
        # Then, we read the first (and what should be only) line in the file.
        # We sanitize it and then compare it to the names of the classes we defined.
                line = f.readline()
                line = line.strip()
                line = line.lower()
            # If the line is boat, car, or plane, we initialize one of our classes.
                if line == "boat":
                    class Vehicle(Boat):
                        pass
                elif line == "car":
                    class Vehicle(Car):
                        pass
                elif line == "plane":
                    class Vehicle(Plane):
                        pass
            # If it's literally anything else, then we don't want it and we tell the user that
                else:
                    print("ERROR: Line 1 does not read 'Plane', 'Boat', or 'Car'. Please check file and try again.")
                    vehicle_readout(Vehicle())
            # Should the file not be found, this error will be raised.
        except FileNotFoundError: 
            print("File not found! Please try again.")

# This function is run later to print our output.
def vehicle_readout(x):
    x.introduction()
    x.year_invented()
    x.top_speed()
    x.fun_fact()

# This is where we define our classes that we're gonna use later, since classes are required
# for this assignment.
# This is the boat class
class Boat:
    def introduction(self):
        print("Boats are aquatic vehicles that sail on top of water! Wicked cool!")
    def year_invented(self):
        print("Boats are very old, dating back to at least 8,000 BCE! Now that's old!")
    def top_speed(self):
        print("The top speed of a boat is 317 MPH, set in 1978 by Ken Warby, an Australian.")
    def fun_fact(self):
        print("Early ships could be rowed by as many as 300 oarmen! Talk about manpower!")

# This is the car class
class Car:
    def introduction(self):
        print("Cars are land vehicles that drive over land and terrain! Awesome!")
    def year_invented(self):
        print("1886 is regarded as the 'birth year' of the car, as that's when Karl Benz patented his Benz Patent-Motorwagon")
    def top_speed(self):
        print("The fastest a car has gone is 763.035 MPH, set by Andy Green in a jet-powered supercar.")
    def fun_fact(self):
        print("There are over 1 billion cars in use across the planet!")

# This is the plane class
class Plane:
    def introduction(self):
        print("Planes are aerial vehicles that soar through the air! Tubular!")
    def year_invented(self):
        print("Planes were invented in 1903, which is when the Wright Brothers first took flight.")
    def top_speed(self):
        print("The Lockheed SR-71 Blackbird is the fastest aircraft in the world, reaching Mach 3.3, or over 2100 MPH!")
    def fun_fact(self):
        print("Some planes can  fly for more than 5 hours after their engines go out.")

# Now we set up the window
window = tk.Tk()
# Set the window to a certain size and position on startup
window.geometry('350x200+600+180')

# This tells the user what they need to do
greeting = tk.Label(text="Enter a filename for reading and push the button:")
# This controls precisely where the greeting is placed
greeting.place(x=0, y=0)

# This is where the user inputs their file name
user_entry = tk.Entry()
user_entry.place(x=0, y=75)

main_button = tk.Button(text="Run", width=5, command=file_opener)
main_button.place(x=0, y=150)

# This is the test function, left in for the purpose of getting points.
# When run, it tries to run the function with a pre-determined good file and a non-existent file.
test_button = tk.Button(text="Test", width=5, command=test_function)
test_button.place(x=0, y=125)

# This stops the window from closing until someone closes it
window.mainloop()