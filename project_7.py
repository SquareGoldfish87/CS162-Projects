#!/usr/bin/env python3

"""Make a racing "game" that invokes and handles custom errors and then crashes."""

# To begin, I need random for some fun things later.
import random

# Then, we'll create some custom functions.
#error_thrower lets us pass our Class into it and have it run our error checks 
# (AKA, this is where the main code is run.)
def error_thrower(vehicle):
    """Take the given class and display it's information."""
    print("Welcome to Ridge Racer! Original names are not our strongsuit!")
    print("Get ready to rumble! Here we go!!!")
    # We try to invoke the given Class's ErrorThrow1, and except a BrokenPartError
    try:
        vehicle.ErrorThrow1()
    # If we catch a BrokenPartError (and we always should) then we continue.
    # There's also a .randrange call in here to determine what "place" the user is in.
    # (It doesn't affect any of the other code, if you were wondering)
    except BrokenPartError:
        print(f"You manage to fix it and push onward! You're now in {random.randrange(4, 8)}th place!")
    # Then we try to invoke ErrorThrow2, and have a NoSteeringError as the exception.
    try:
        vehicle.ErrorThrow2()
    # If we catch a NoSteeringError (which, again, should always happen), then we continue.
    except NoSteeringError:
        print(f"Despite the setback, you manage to pull ahead! Now you're in 2nd place!")
    print("So close to the finish line!")
    # Then we invoke ErrorThrow3, which will always crash the code.
    vehicle.ErrorThrow3()

# This function is for testing. It runs the above function on all 3 vehicle types.
# Note: This function was a lot more helpful when the 3rd error wasn't a guaranteed crash.
def test(x, y, z):
    """Run error_checker on the 3 inputted items."""
    error_thrower(x)
    error_thrower(y)
    error_thrower(z)

# Then, we need the custom errors we're going to raise.
# This error will be raised and handled first, and represents a broken part of the vehicle.
class BrokenPartError(Exception):
    pass

# This error will be second, and represents a loss of steering in some way.
class NoSteeringError(Exception):
    pass

# This is the third error, and the one we won't be handling. It represents... I dunno,
# an explosion or something.
class EverythingBreaksError(Exception):
    pass


# Then, we create our custom instances of classes.
# All 3 classes have an ErrorThrow 1, 2, and 3.
# Each of these ErrorThrows assigns an impossible circumstance, and as long as it remains
# impossible (it always will), it raises one of our custom errors.
# It's worth noting that ErrorThrow3 will always crash the program.
class Boat:
    def ErrorThrow1(self):
        print("The motor has stopped!")
        x = 3
        if x != 42:
            raise BrokenPartError
    def ErrorThrow2(self):
        print("Your rudder is snapped!")
        x = 5
        if x != 6:
            raise NoSteeringError
    def ErrorThrow3(self):
        x = 2
        if x == 2:
            raise EverythingBreaksError("An explosion! BOOM!!!! Your race is over.")

class Bike:
    def ErrorThrow1(self):
        print("Your pedal has broken!")
        x = 3
        if x != 42:
            raise BrokenPartError
    def ErrorThrow2(self):
        print("The handlebars have come off!")
        x = 5
        if x != 6:
            raise NoSteeringError
    def ErrorThrow3(self):
        x = 2
        if x == 2:
            raise EverythingBreaksError("An explosion! BOOM!!!! Your race is over.")

class Plane:
    def ErrorThrow1(self):
        print("One of the wing flaps is down!")
        x = 3
        if x != 42:
            raise BrokenPartError
    def ErrorThrow2(self):
        print("Your steering wheel locked up!")
        x = 5
        if x != 6:
            raise NoSteeringError
    def ErrorThrow3(self):
        x = 2
        if x == 2:
            raise EverythingBreaksError("An explosion! BOOM!!!! Your race is over.")

# Now we initialize our classes
boat = Boat()
bike = Bike()
plane = Plane()

# This gives the user a random vehicle every time they run the program.
# We add all the instances of our classes to a list
vehicle_list = [boat,bike,plane]
# We make a variable with a random value that's either 0, 1, or 2
random_num = random.randrange(0, 2)
# We use our random_num to find the item in the list at the index random_num
current_vehicle = vehicle_list[random_num]

# Then we run the function with the main code in it, passing in our random vehicle.
error_thrower(current_vehicle)