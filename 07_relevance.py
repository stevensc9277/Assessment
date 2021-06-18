import math
import turtle
import numpy

# draws a triangle using given parameters
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
  turtle.setpos(displacement[0] * 15, 0)
  turtle.write('B', font = 'style', align = 'left')
  turtle.setpos(displacement[0]*10, 0)
  tess.forward(displacement[1] * 10)
  tess.left(180 - angle[1])
  turtle.setpos(displacement[2]* 10 * math.cos(math.radians(some_angles[1])), some_lengths[2]* 10 * math.sin(math.radians(some_angles[1]))) 
  # y-axis is vertical height, x is distance from point B to C (horizontal), need function to find y (constantly changes)
  turtle.write('C', font = 'style', align = 'center')
  tess.forward(displacement[2] * 10)
   # Complete the triangle

  # tess.right(180)  # Turn tess around
  # tess.forward(80)  # Move her away from the origin
  turtle.exitonclick()

  wn.mainloop()


# checks user input is an integer or float
def num_check(question, low, high, type):
  error = "Please enter a number more than {} or less than {}".format(low, high)

  while True:
    try:
      response = type(input(question))

      if response <= low:
        print(error)
        print()
      
      elif response >= high:
        print(error)
        print()
      else:
        return response
    
    except ValueError:
      print(error)
      print()

# used mostly for yes / no questions
def string_checker(question, to_check):
  error = "Sorry that is not a valid response"

  while True:

    # ask question and put response in lowercase
    response = input(question).lower()
    if response in to_check:
      return response

    else:
      for item in to_check:
        # checks if response is the first letter of an item in the list
        if response == item[0]:
          # return the entire response rather than just the first letter
          return item
      print(error) 

# Length or angle checker
def how_many(question, length_or_deg):
  global some_angles
  global some_lengths
  repeats = num_check(question, 0, 3, int)
  for item in range(0, repeats): 
    if length_or_deg[0] == "l":
      angles_length = num_check("How long? ", 0, 150, float)
      some_lengths.append(angles_length)
    
    else:
      angles_length = num_check("How many degrees? ", 0, 150, float)
      some_angles.append(angles_length)

   
# Lists for variables
some_angles = []
some_lengths = []

anglength_dict = {
  'Angles': some_angles,
  'Lengths': some_lengths
}


# Ask for angles and lengths
angles = how_many("How many angles do you know? ", "degrees")
print()
lengths = how_many("How many lengths do you know? ", "long")
not_angle = 0

# Identify number of variables known
known_ang = len(some_angles)
known_len = len(some_lengths)

if known_len == 3 and known_ang == 0:
  print("Total perimeter is ", sum(some_lengths))
  print("There was not enough information to find the area")
  print("Click the drawing to continue the program")
  draw = triangle([10, 10, 10], [60, 60, 60])

elif known_len == 2 and known_ang >= 1:
  # identify positions of angles and lengths
  for i in some_angles:
    inc_angle = string_checker("Is the angle {} between the two lengths? ".format(i), ["yes", "no"])
    if inc_angle == "yes":
      # find missing angle
      angle = 180 - sum(some_angles)

      # find missing side
      side_square = pow(some_lengths[0], 2) + pow(some_lengths[1], 2) - 2*(numpy.prod(some_lengths)) * math.cos(math.radians(some_angles[0]))
      side_own = math.sqrt(side_square)
      side_own = round(side_own, 2)
      print("Unknown length is ", side_own)
      some_lengths.append(side_own)
      some_angles.append(angle)
      break
    else:
      not_angle += 1
      continue
      
    if not_angle == 3:
      print("Something is wrong with your input, we need to start again")

elif known_len == 1 and known_ang == 1:
  print("Not enough information")
  print("end")
    
draw = triangle(some_lengths, some_angles)