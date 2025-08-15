# 54.py
# Han Rockhill
# python 3.12.2
# 04/30/2024

# Write 3 programs
# 1.) Rectangle.py
# 2.) Triangle.py
# 3.) boxNoCorners.py

# 1.) Rectangle.py
# Create a new canvas using turtle module's Pen function and then draw a rectangle
import turtle

# Define the square
def drawSquare():
    pen = turtle.Turtle()
    loops = 4
    distance = 80
    angle = 90
    for _ in range(loops):
        pen.forward(distance)
        pen.right(angle)

    turtle.Screen().clear()  # Close the screen after drawing square

# Create the first screen for the square
screen_square = turtle.Screen()

# Call the function drawSquare
drawSquare()

# Define the triangle
def drawTriangle():
    pen = turtle.Turtle()
    loops = 3
    distance = 80
    angle = 120
    for _ in range(loops):
        pen.forward(distance)
        pen.right(angle)

    turtle.Screen().clear()  # Close the screen after drawing triangle

# Create the second screen for the triangle
screen_triangle = turtle.Screen()

# Call the function drawTriangle
drawTriangle()

# Define the no corner box
def drawNoCornerBox():
    pen = turtle.Turtle()
    loops = 4
    distance = 80
    gap = 20
    angle = 90
    for _ in range(loops):
        pen.forward(distance)
        pen.penup()
        pen.forward(gap)
        pen.right(angle)
        pen.penup()
        pen.forward(gap)
        pen.pendown()


# Create the screen for the no corner box
screen_noCorner = turtle.Screen()

# Call the function drawNoCornerBox
drawNoCornerBox()

screen_noCorner.mainloop()

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Documents/54.py =====================
'''