#!/usr/bin/env python3
"""Create a GUI that displays 100 rectangles and sorts them when the user pushes a button."""

# It is again worth noting that this code does not work. I have edited it so that it will run, but the desired outcome
# not achieved. I did get pretty close though.

# First, we need to import tkinter and random
import tkinter as tk
import random

# This function handles rectangle creation.
def rectangle_maker(list:list):
    """Create 100 rectangles and append number values to them."""
    # We start by defining values.
    # Index handles the number of squares.
    index = 0
    # row_tracker keeps track of the horizontal positioning of the rectangles, and
    # is used to move the rectangles by a set amount.
    row_tracker = 0
    # column_tracker is row_tracker but for the vertical positioning.
    column_tracker = 0
    # While our index isn't 100 (the number of squares we create/search), we add to it,
    # update row_checker, and check to see if the index modulo 10 is 0.
    while index != 100:
        index+=1
        row_tracker += 15
        if index % 10 == 0:
         # If so, there are 10 squares in this row, so we update column_checker, bump down
         # a level, and reset row_checker so that the row starts from the left.
            column_tracker += 25
            row_tracker = 0
        # Then we draw our rectangles.
        drawing.create_rectangle(25+row_tracker, 50+column_tracker, 10+row_tracker, 70+column_tracker)
        # At the same time, we create textboxes over the rectangles with the numbers from the list in them.
        box_num = tk.Label(text=f"{list[index-1]}", bg="yellow")
        box_num.place(x=10+row_tracker, y=50+column_tracker)

# Now we need our list of numbers.
# A new index for this list.
num_list_index = 0
# The actual list
num_list = []
# Make a random number between 1-100, add it to the list, and do it 100 times.
while num_list_index != 100:
    num_list_index += 1
    num_list.append(random.randrange(1, 100))
# The below line was for testing, but I'm leaving it in. Uncomment it to make the squares sorted.
#num_list.sort()

# Now we set up the window
window = tk.Tk()
# Set the window to a certain size and position on startup
window.geometry('350x450+600+180')

# Make the window use the Canvas widget
drawing = tk.Canvas(window, width=800, height=600)
drawing.grid(column=0, row=0)
# Call the function to create the rectangles and pass in our random list
rectangle_maker(num_list)

# This displays a greeting message
greeting = tk.Label(text="Press the button and I'll sort the numbers!")
# This controls precisely where the greeting is placed
greeting.place(x=0, y=0)

# A button to actually start the sort. When pushed, the button calls .sort on the list and calls the function again.
button = tk.Button(text="Sort", width=5, command=rectangle_maker(num_list))
button.place(x=250, y=350)

# Without getting too much into it, the code runs fine when this isn't here, but I decided to leave it in and 
# comment it out.
#button = tk.Button(text="Test", width=5, command=rectangle_maker(num_list))
#button.place(x=250, y=400)

# This ensures the window stays open until closed
window.mainloop()

# Here I'll explain what went wrong. Basically, if a button is issued a function command that takes an argument, it'll
# run that function on startup. Thus, I couldn't just set the button to run .sort on the list and make the rectangles 
# again. A button also can't run a function that runs .sort, for some weird reason. Every time I tried it either
# didn't work or it threw a TypeError. The first problem was easy enough to fix. Just make a dev button that runs the
# correct parameters on startup, and leave the regular button as-is for the user to sort stuff. That's why there's a second
# button above. The other problem, I figured, could be solved if I could make my own sorting function that didn't return
# None so it would work in subscript (which is such a bizarre error, but I digress). Unfortunately, I just can't seem to
# be able to make one. I know that it should be relatively simple and if I remembered more about basic list indexing and
# such, it wouldn't be a problem. Alas, I do not remember these things, and Ol' Reliable (Googling it) has provided nothing.

# In summary, just like last time, if I could get the button to work and make a simple function call then it would run, but
# I cannot, despite my best efforts. Here's what I managed to get done, and I hope it counts for something.
# Also, apologies for the messiness of the squares. I planned to clean it up when I had time, but that seems to be in 
# rather short supply these days.