import turtle

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
   
  tess.forward(displacement[0] * 10)  # Make tess draw a triangle
  tess.left(180 - angle[0])
  tess.forward(displacement[1] * 10)
  tess.left(180 - angle[1])
  tess.forward(displacement[2] * 10)
  tess.left(180 - angle[2])  # Complete the triangle

  tess.right(180)  # Turn tess around
  tess.forward(80)  # Move her away from the origin


  wn.mainloop()

to_draw = triangle([5, 5, 5], [60, 60, 60])