import math
import turtle
import time

# draws a triangle using given parameters
def triangle(displacement, angle):
  # initialise turtles
   # Set up the window and its attributes
  wn = turtle.Screen()
  # This just makes the screen full screen without the user having to touch the maximize button repeatedly
  wn.setup(width=1.0, height=1.0, startx=None, starty=None)
  wn.bgcolor("lightgreen")
  wn.title("Triangle")
  
  tess = turtle.Turtle()  # Create tess and set some attributes
  tess.color("black")
  tess.pensize(5)
  turtle.write('A', font = 'style', move = True, align = 'right')
  tess.forward(displacement[0] * 10)  # Make tess draw a triangle
  tess.left(180 - angle[0])
  turtle.setpos(displacement[1] * 10, 0)	
  turtle.write('B', font = 'style', align = 'left')	
  turtle.setpos(displacement[1]*10, 0)	
  tess.forward(displacement[1] * 10)	
  tess.left(180 - angle[1])	
  turtle.setpos(displacement[0]* 5, math.sin(math.radians(angle[0])) * displacement[1] * 10) # y-axis is vertical height, x is half of line AB, need to function to find y (constantly changes)	
  turtle.write('C', move = True, font = 'style', align = 'center')	
  tess.forward(displacement[2] * 10)
   # Complete the triangle

  # tess.right(180)  # Turn tess around
  # tess.forward(80)  # Move her away from the origin
  time.sleep(5)
  turtle.reset()
  tess.reset()
  
 
draw = triangle([10, 10, 10], [60, 60, 60])

triangle([20, 20, 20], [60, 60, 60])
turtle.exitonclick()