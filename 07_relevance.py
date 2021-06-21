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
  turtle.exitonclick()

  wn.mainloop()


# checks user input is an integer or float
def num_check(question, low, high, type, error):

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

   
# Lists for variables
some_angles = []
some_lengths = []

remember = 0
not_angle = 0
right_wrong = 0
anglength_dict = {
  'Angles': some_angles,
  'Lengths': some_lengths
}


# Ask for angles and lengths
ang_in = num_check("How many angles do you know? ", 0, 3, int,"At least 1 angle is needed to continue")

# Make sure there are enough variables to continue
if ang_in == 1:
  inc_angle = string_checker("Is the angle an inclusive angle (between two lengths)? ", ["yes", "no"])
  len_in = num_check("How many lengths do you know? ", 1, 3, int, "At least 2 lengths are needed to continue")

else:
  len_in = num_check("How many lengths do you know? ", 1, 3, int, "At least 1 length is needed to continue")
  

# Getting angle and length values
for i in range(0, ang_in):
  angle = num_check("How many degrees? ", 0, 150, float, "Please enter a number more than 0 or less than 150")
  some_angles.append(angle)

for i in range(0, len_in):
  length = num_check("How long? ", 0, 100, float, "Please enter a number more than 0 or less than 100")
  some_lengths.append(length)

# Identify number of variables known
known_ang = len(some_angles)
known_len = len(some_lengths)

# First case: 3 lengths, 1 angle or no angle
if known_len == 3 and known_ang == 0:
  print("Total perimeter is ", sum(some_lengths))
  print("There was not enough information to find the area")
  print("Click the drawing to continue the program")
  draw = triangle([10, 10, 10], [60, 60, 60])

elif known_len == 3 and known_ang == 1:
  # inc angle rule for area and perimeter just add all lengths
  for i in some_angles:
    inc_angle = string_checker("Is the angle {} an inclusive angle between your two lengths? ".format(i), ["yes", "no"])
    if inc_angle == "yes":
      # find missing angle
      angle = 180 - sum(some_angles)

      # find missing side
      side_square = pow(some_lengths[0], 2) + pow(some_lengths[1], 2) - 2*(numpy.prod(some_lengths)) * math.cos(math.radians(i))
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
      print("Something is wrong with your information because none of the lines have the angle in between them")
      print("Click the drawing to start again")
      break

elif known_len == 2 and known_ang == 1:
  for i in some_angles:
    inc_angle = string_checker("Is the angle {} an inclusive angle between your two lengths? ".format(i), ["yes", "no"])
  if inc_angle == "yes":
    # find missing angle
    angle = 180 - sum(some_angles)

    # find missing side
    side_square = pow(some_lengths[0], 2) + pow(some_lengths[1], 2) - 2*(numpy.prod(some_lengths)) * math.cos(math.radians(i))
    side_own = math.sqrt(side_square)
    side_own = round(side_own, 2)
    print("Unknown length is ", side_own)
    some_lengths.append(side_own)
    some_angles.append(angle)
   
  else:
    # not an inclusive angle so it must be opposite a length
    for a,b in zip(some_angles, some_lengths):
      opposite = string_checker("Is the angle {} opposite the line which is {} units long? ".format(a, b), ["yes", "no"])

      if opposite == "yes":
        # find position in list
        pos = some_lengths.index(b)
        confusion = (pos - right_wrong) * -1
        # find all angles from here
        in_bracket = some_lengths[pos]  * (math.sin(math.radians(a))) / some_lengths[pos]
        ang_opp_other = math.asin(math.radians(in_bracket))
        print(ang_opp_other)
      

      else:
        right_wrong += 1
        pos = some_lengths.index(i)
        confusion = (pos - right_wrong) * - 1
        # find all angles from here
        in_bracket = some_lengths[pos]  * (math.sin(math.radians(some_angles[0]))) / some_lengths[pos]
        ang_opp_other = math.asin(math.radians(in_bracket))
        print(ang_opp_other)

elif known_ang == 2 and known_len == 1:
  missing_angle = 180 - sum(some_angles)
  # Use sine rule
  for i in some_angles:
      opposite = string_checker("Is the angle {} opposite the line which is {} units long? ".format(i, some_lengths[0]), ["yes", "no"])

      if opposite == "yes":
        # find position in list
        pos = some_angles.index(i)
        confusion = (pos - right_wrong) * -1
        # find all angles from here
        in_bracket = some_lengths[pos]  * (math.sin(math.radians(a))) / some_lengths[pos]
        ang_opp_other = math.asin(math.radians(in_bracket))
        print(ang_opp_other)
      

      else:
        right_wrong += 1
        pos = some_lengths.index(i)
        confusion = (pos - right_wrong) * - 1
        # find all angles from here
        in_bracket = some_lengths[pos]  * (math.sin(math.radians(some_angles[0]))) / some_lengths[pos]
        ang_opp_other = math.asin(math.radians(in_bracket))
        print(ang_opp_other)

  some_angles.append(missing_angle)
draw = triangle([10, 10, 10], [60, 60, 60])