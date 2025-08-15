# 55.py
# Han Rockhill
# python 3.12.2
# 04/30/2024
# draw a face

import turtle
# going to (-40,110), DRAW LEFT EYE
draw = turtle.Turtle()
draw.penup()
draw.goto(-40, 110)
draw.pencolor("blue") # change the color of the pen
draw.pendown() # put the pen down
draw.circle(10) # this draw a circle with a radius of 10
draw.penup()

# going to (40,110), DRAW RIGHT EYE
draw = turtle.Turtle()
draw.penup()
draw.goto(40, 110)
draw.pencolor("green") # change the color of the pen
draw.pendown() # put the pen down
draw.circle(10) # this draw a circle with a radius of 10

# going to (0,50), DRAW SMILE
draw.penup()
draw.goto(0, 0)
draw.pencolor("red") # change the color of the pen
draw.pendown() # put the pen down
draw.circle(100, -75)
draw.circle(100, 150)

# going to (0,110), DRAW NOSE BROWN
draw.penup()
draw.goto(0,110)
draw.pendown()
draw.pencolor("brown")
draw.right(165)
draw.forward(45)
draw.left(90)
draw.forward(10)

# going to (-120,95), DRAW HEAD
draw.penup()
draw.right(90)
draw.goto(-120,95)
draw.pendown()
draw.pencolor("black")
draw.circle(120)

# keep the canvas open so we can see it
turtle.mainloop()


'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Documents/55.py =====================
'''