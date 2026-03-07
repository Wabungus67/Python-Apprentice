"""
Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

forwards = [ 30, 25, 20, 15, 10, 5 ]
lefts = [ 5, 10, 15, 20, 25, 30 ]
colors =   [ 'red', 'orange', 'yellow', 'green', 'blue', 'purple' ]

joe = 0

for  i in range(1000):

    forward = forwards[joe]
    left = lefts[joe]
    color = colors[joe]

    joe = joe + 1

    if joe > 5:
        joe = 0

    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  