import turtle


turtle.hideturtle()
# function for drawing the triangle
def triangle(displacement, angle):
  # initialise turtles
  wn = turtle.Screen()  # Set up the window and its attributes

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
  turtle.setpos(displacement[2]* 5, 86) # y-axis is vertical height, x is half of line AB, need to function to find y (constantly changes)
  turtle.write('C', move = True, font = 'style', align = 'center')
  tess.forward(displacement[2] * 10)
   # Complete the triangle

  # tess.right(180)  # Turn tess around
  # tess.forward(80)  # Move her away from the origin


  wn.mainloop()


to_draw = triangle([10, 10, 10], [60, 60])