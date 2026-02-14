"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(200)                       # Move tina forward by the forward distance
tina.right(120)                          # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(120) 

tina.pencolor('green')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(120)  # Your code here

turtle.exitonclick()                    # Close the window when we click on it