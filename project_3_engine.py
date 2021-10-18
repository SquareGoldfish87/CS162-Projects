#!/usr/bin/env python3
"""Create a GUI that allows a user to interact with the "engine" of our group's "car"."""
# This is one of three pieces of the larger "car" I'm making for Project 3.

# First, we import tkinter
import tkinter as gui

# Next, we make the window itself
window = gui.Tk()
# This alters the window's color
window.configure(bg="#098")
# Set the window to a certain size and position on startup
window.geometry('350x450+600+180')

# Some variables we'll need later:
# current_speed keeps track of the last entered speed value
current_speed = 0
# ignition_state keeps track of whether the car is on or off
ignition_state = "off"
# car_color keeps track of the car's color
car_color = "Red"

# This function displays whether the car is on or off.
# For now, it's always "off".
def ignition_checker(ignition_state):
    return gui.Label(window, text=f"The car is now {ignition_state}").place(x=0, y=75)

# This function displays the last entered speed.
# For now, it's always 0.
def speed_displayer():
    return gui.Label(window, text=f"The car's current speed is {current_speed} MPH").place(x=0, y=125)

# This function displays the car's color.
# For now, it's always "Red".
def color_displayer():
    return gui.Label(window, text=f"The car's current color is {car_color}").place(x=0, y=175)


# This displays a greeting message
greeting = gui.Label(text="Welcome to EnginePy! Please select an option: ")
# This controls precisely where the greeting is placed
greeting.place(x=0, y=0)

# This lets the user start and stop the car
ignition_button = gui.Button(window, text="Push me to start/stop the car!", command=ignition_checker(ignition_state))
ignition_button.place(x=0, y=50)

# This lets the user display the last entered speed
speed_display = gui.Button(text="Push this button to display current speed!", command=speed_displayer)
speed_display.place(x=0, y=100)

# This lets the user display the car's color
color_button = gui.Button(window, text="Click me to see the car's current color!", command=color_displayer)
color_button.place(x=0, y=150)

# This keeps the window open until it's closed. 
window.mainloop()