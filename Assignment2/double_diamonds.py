import turtle 

# predefine the diamond side length 
SIDE_LENGTH = 100

# predefine the fill color 
COLOR = "blue" 

# setup the turtle window 
turtle.setup(500, 600) 

# setup the turtle 
turtle.hideturtle()          # hide the turtle cursor so only the drawing shows
turtle.fillcolor(COLOR)      # set the fill color to blue

# draw the left-side diamond first using the predefined SIDE_LENGTH 
turtle.penup()               # lift the pen so moving doesn't draw a line
turtle.goto(-100, 0)         # move to the left vertex of the left diamond 
turtle.setheading(45)        # face up-right (45°) so we draw the top-right side first 
turtle.pendown()             # put the pen down to start drawing
turtle.begin_fill()          # start filling the shape with the chosen color
for _ in range(4):           # a diamond has 4 equal sides
    turtle.forward(SIDE_LENGTH)   # draw one side
    turtle.right(90)              # turn 90° right to create the diamond's corner
turtle.end_fill()            # finish filling the shape
# draw the right-side diamond next 
turtle.penup()               # lift the pen again before repositioning
turtle.goto(0, 0)            # move to the left vertex of the right diamond (shared with left's right vertex) 
turtle.setheading(45)        # face the same 45° direction for consistency
turtle.pendown()             # put the pen down to draw
turtle.begin_fill()          # start filling the second diamond
for _ in range(4):           # repeat 4 times for the 4 sides
    turtle.forward(SIDE_LENGTH)   # draw each side at the same length
    turtle.right(90)              # turn 90° right each time to form the diamond
turtle.end_fill()            # finish filling the second shape
turtle.done()                # keep the window open until the user closes it