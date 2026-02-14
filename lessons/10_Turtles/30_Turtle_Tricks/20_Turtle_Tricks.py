"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(800,800,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(200)                       # Move tina forward by the forward distance
tina.right(72)                          # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(72) 

tina.pencolor('green')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(72)

tina.pencolor('orange')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(72)

tina.pencolor('purple')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(72) # Your code here

turtle.exitonclick()                    # Close the window when we click on it