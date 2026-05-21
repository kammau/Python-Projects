import tkmacosx # GUI Library
import tkinter
from tkmacosx import Button

# 2D List: Structure of button's layout (5 rows and 4 columns)
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# Operators
right_symbols = ["÷", "×", "-", "+", "="]
# Functions
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) # 5 rows in 2D list button_values
column_count = len(button_values[0]) # 4 columns in 2D list button_values (for each inner list)

# Color's for calc using hexidecimal values (except white)
color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white" # Basic color in tkmacosx color's (so just name)

# Window Setup
window = tkinter.Tk() # Create the window
window.title("Calculator") # Title for window
window.resizable(False, False) # User CANNOT resize window (False for width and false for height)

frame = tkinter.Frame(window) # Place frame inside window
# label -> (parent, text within, font (style and size), background color, font color, place text to right side (east))
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black, foreground=color_white, anchor="e")

# columnspan=column_count have label fill columns
# sticky="we" stretch west to east
label.grid(row=0, column=0, columnspan=column_count, sticky="we") # Indicates which row and column to place label

# Iterate through each row and column of the button_values list
# Create a button for each button_value item
for row in range(row_count):
    for column in range(column_count):
        # Get specific button_value
        value = button_values[row][column]
        # Create button using tkmacosx
        #.Button(place button into frame, text to put in button, font style and size, width and height of button, what to do when button is clicked)
        # Width & Height in tkmacosx are measured by SCREEN UNITS not pixels
        # LAMBDA: lambda arguments: expression
        button = Button(frame, text=value, font=("Arial", 30), width=column_count-1, height=1, command=lambda value=value: button_clicked(value))

        # Change colors depending on button
        # If button is a top symbol
        if value in top_symbols:
            # Configure button color font to black and background to gray
            button.config(foreground=color_orange, background=color_light_gray)
        # Else if button is a right symbol
        elif value in right_symbols:
            # Configure button color font to white and background to orange
            button.config(foreground=color_white, background=color_orange)
        # Else for the rest of the buttons
        else:
            button.config(foreground=color_white, background=color_dark_gray)

        # Where to place button in grid
        button.grid(row=row+1, column=column)

frame.pack()

# Func called when button is clicked
def button_clicked(value):
    pass

window.mainloop() # Tells tkmacosx to enter an infinite loop that constantly monitors for events.