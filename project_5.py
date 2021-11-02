#!/usr/bin/env python3
"""Create a GUI that displays 100 rectangles and searches for a specific rectangle based on
user input."""

# I'll let you know now, the code doesn't entirely work. The button doesn't do anything, so no search can occur.
# Because of that, I haven't quite been able to test things to the fullest extent (it's hard to test code when
# you have no easy way to run most of it). However, I hope that what *is* here is enough for some partial
# points.

# First, we need to import tkinter
import tkinter as tk

# This function handles rectangle creation and list enumeration, since I wanted both to
# use the same index value and this was the easiest (albeit convoluted) way.
# The function takes 2 arguments: The list we're searching and the number we're looking for.
def rectangle_maker(list:list, user_value):
    """Create 100 rectangles, as well as search a list."""
    # We start by defining values.
    # Index handles the number of squares, as well as the list's index we're searching.
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
        # If so, there are 10 squares in this row, so we update column_checker, bump down
        # a level, and reset row_checker so that the row starts from the left.
        if index % 10 == 0:
            column_tracker += 25
            row_tracker = 0
        # Then we draw our rectangles.
        drawing.create_rectangle(25+row_tracker, 50+column_tracker, 10+row_tracker, 70+column_tracker, fill="yellow")
        # Piggybacking off of the prior index, if the user's number is in the list at
        # that index, we've found our square. So we turn it green, and print that
        # we've found it
        for index in list:
            if index == user_value:
                    drawing.create_rectangle(25+row_tracker, 50+column_tracker, 10+row_tracker, 70+column_tracker, fill="green")
                    # Since the index is off by 1, we add 1 as we print it.
                    print(f"Found {user_num} at rectangle {index+1}!")
            # If it's not at that square, then we turn that square red and move on
            else:
                drawing.create_rectangle(25+row_tracker, 50+column_tracker, 10+row_tracker, 70+column_tracker, fill="red")

# Now we need our list of numbers.
# A new index (it makes no difference but it helps legibility)
num_list_index = 0
# The actual list
num_list = []
# Add every number from 1-100 inclusive to num_list
while num_list_index != 100:
  num_list_index += 1
  num_list.append(num_list_index)


# Now we set up the window
window = tk.Tk()
# Set the window to a certain size and position on startup
window.geometry('350x450+600+180')

# Make the window use the Canvas widget
drawing = tk.Canvas(window, width=800, height=600)
drawing.grid(column=0, row=0)
# Call the function to create the rectangles and pass in variables that don't do
# anything.
rectangle_maker([], 5)

# This displays a greeting message
greeting = tk.Label(text="Enter a number below and I'll find it for you!")
# This controls precisely where the greeting is placed
greeting.place(x=0, y=0)

# Add a box for the user to enter their number
user_num = tk.Entry()
user_num.place(x=0, y=350)

# A button to actually start the search
button = tk.Button(text="Search", width=5, command=rectangle_maker([], user_num.get()))
button.place(x=250, y=350)

# This ensures the window stays open until closed
window.mainloop()