import math
import turtle
import numpy
import pandas

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
  turtle.setpos(displacement[2]* 5, math.sin(math.radians(some_angles[0])) * some_lengths[1] * 10) # y-axis is vertical height, x is half of line AB, need to function to find y (constantly changes)	
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

# find a missing angle using sine rule
def find_angle(find, angle):
  pos = some_lengths.index(i)
  confusion = (pos - 1) * -1
  # find all angles from here
  fraction = some_lengths[confusion] / some_lengths[pos]
  
  product = fraction * math.sin(math.radians(some_angles[0])) 
  
  ang_opp_other = round(math.degrees(math.asin(product)), 2)
  
  
  some_angles.append(ang_opp_other)
  last_ang = 180 - sum(some_angles)
  some_angles.append(last_ang)
 

# find area using Heron's law instead of inclusive angle   
def find_area(angle):
  print("Imagine an arc between your two lengths while the triangle is placed vertically")
  print()
  index = 0
  other_index =  1
  # iterate 2 items at a time using a for loop
  for i in some_lengths:
    if index >= 2:
      other_index = 0
      break
      
    what_are_inc = string_checker("Do the lines which are {} and {} units long have the angle between them? ".format(some_lengths[index], some_lengths[other_index]), ["yes", "no"])
    
    
    if what_are_inc == "yes":
      # area = 0.5 * bc * sin A
      area = 0.5 * some_lengths[index] * some_lengths[other_index] * math.sin(math.radians(angle))
      return round(area, 2)
    index += 1 
    other_index += 1

# Lists for variables
some_angles = []
some_lengths = []
item = 0

not_angle = 0
anglength_dict = {
  'Angles': some_angles,
  'Lengths': some_lengths,
  'Lines': ["AB", "BC", "CA"]
}

# instructions go here
print("These are your instructions...")
print("All lengths are required to have the same units as I am too lazy to do the conversions for you (Help me help you)")

start = input("Input any key to continue. ")

# main program starts here
keep_going = ""
while keep_going == "":
  # Ask for angles and lengths
  ang_in = num_check("How many angles do you know? ", 0, 3, int,"At least 1 angle is needed to continue")

  # Make sure there are enough variables to continue
  if ang_in == 1:
    len_in = num_check("How many lengths do you know? ", 1, 3, int, "At least 2 lengths are needed to continue")

  else:
    len_in = num_check("How many lengths do you know? ", 0, 4, int, "At least 1 or 3 lengths are needed to continue")
    

  # Getting angle and length values
  while item != ang_in:
    angle = num_check("How many degrees? ", 0, 150, float, "Please enter a number more than 0 or less than 150")
    some_angles.append(angle)
    print()
    item += 1
    # can't enter angles with a sum greater than 180
    if sum(some_angles) >= 180:
      print("Total angle cannot be more than 180 degrees. Please try again")
      some_angles.clear()
      print()
      item = 0
      continue

  for i in range(0, len_in):
    length = num_check("How long? ", 0, 100, float, "Please enter a number more than 0 or less than 100")
    some_lengths.append(length)
    print()

  # Identify number of variables known
  known_ang = len(some_angles)
  known_len = len(some_lengths)

  # First case: 3 lengths, 1 angle or no angle
  if known_len == 3 and known_ang == 0:
    print("Total perimeter is ", sum(some_lengths))
    print("There was not enough information to find the area")
    print("Click the drawing to continue the program")
    draw = triangle([10, 10, 10], [60, 60, 60])


  # Achieved 3 lengths, 3 angles, perimeter and area
  elif known_len == 3 and known_ang == 1:
    # use sine rule to find other angles
    for i in some_lengths:
        opposite = string_checker("Is the angle {} opposite the line which is {} units long? ".format(some_angles[0], i), ["yes", "no"])

        if opposite == "yes":
          # use function to find Angles
          an_angle = find_angle(i, some_angles[0])
          break

        else:
          continue

        for i in some_angles:
          inclusive_angle = string_checker("Is the angle {} between your two lengths? ".format(i), ["yes", "no"])
          if inclusive_angle == "yes":
            to_find = find_area(i)
            break
          else:
            continue

  # Achieved 3 lengths, 3 angles, area and perimeter
  elif known_len == 2 and known_ang == 2:
    missing_angle = 180 - sum(some_angles)
    some_angles.append(missing_angle)
    for i in some_angles:
      inclusive_angle = string_checker("Is the angle {} between your two lengths? ".format(i), ["yes", "no"])
      if inclusive_angle == "yes":
        last_side = math.sqrt(pow(some_lengths[0], 2) + pow(some_lengths[1], 2) - 2 * numpy.prod(some_lengths) * math.cos(math.radians(i)))
        some_lengths.append(round(last_side, 2))
        
        to_find = find_area(i)
        break
      else:
        continue

  # Also achieved 3 lengths, 3 angles, area and perimeter
  elif known_len == 2 and known_ang == 1:
    for i in some_angles:
      inc_angle = string_checker("Is the angle {} an inclusive angle between your two lengths? ".format(i), ["yes", "no"])
    if inc_angle == "yes":
      
      # find missing side
      side_square = pow(some_lengths[0], 2) + pow(some_lengths[1], 2) - 2*(numpy.prod(some_lengths)) * math.cos(math.radians(i))
      side_own = math.sqrt(side_square)
      side_own = round(side_own, 2)
      print("Unknown length is ", side_own)
      some_lengths.append(side_own)
      
      # need to find angle next
      # find all angles from here
      fraction = some_lengths[0] / side_own
      
      product = fraction * math.sin(math.radians(some_angles[0])) 
      
      ang_opp_other = round(math.degrees(math.asin(product)), 2)
      
      
      some_angles.append(ang_opp_other)
      last_ang = 180 - sum(some_angles)
      some_angles.append(last_ang)
      # enough info to find area and perimeter
      to_find = find_area(i)

      
    
    else:
      # not an inclusive angle so it must be opposite a length
      for i in some_lengths:
        opposite = string_checker("Is the angle {} opposite the line which is {} units long? ".format(some_angles[0], i), ["yes", "no"])

        if opposite == "yes":
          # use function to find missing angle opposite 1 of the lengths
          an_angle = find_angle(i, some_angles[0])
          break

        else:
          continue
      # enough lengths to find area and perimeter
      for i in some_angles:
        to_find = find_area(i)
          
  # Last to achieve 3 lengths & angles, area and perimeter
  elif known_ang == 2 and known_len == 1:
    missing_angle = 180 - sum(some_angles)
    some_angles.append(missing_angle)
    # Use sine rule
    for i in some_angles:
        opposite = string_checker("Is the angle {:.2f} opposite the line which is {} units long? ".format(i, some_lengths[0]), ["yes", "no"])

        if opposite == "yes":
          # divide known len by angle i and multiply result by other angle in list

          fraction = some_lengths[0]/ math.sin(math.radians(i))
          # find position in list
          pos = some_angles.index(i)
          
          if pos == 0:
            other_side = fraction * math.sin(math.radians(some_angles[1]))
            another_side = fraction * math.sin(math.radians(some_angles[2]))
            some_lengths.append(round(other_side, 2))
            some_lengths.append(round(another_side, 2))
          
          elif pos == 1:
            other_side = fraction * math.sin(math.radians(some_angles[0]))
            another_side = fraction * math.sin(math.radians(some_angles[2]))
            some_lengths.append(round(other_side, 2))
            some_lengths.append(round(another_side, 2))
          
          else:
            other_side = fraction * math.sin(math.radians(some_angles[1]))
            another_side = fraction * math.sin(math.radians(some_angles[0]))
            some_lengths.append(round(other_side, 2))
            some_lengths.append(round(another_side, 2))
          to_find = find_area(i)

          break

    perimeter = sum(some_lengths)
    



  print()
  perimeter = "Perimter is {:.2f} units".format(sum(some_lengths))
  area = "Area is {} units squared".format(to_find)
  print(perimeter)
  print(area)
  print()
  some_lengths.sort(reverse = True)
  some_angles.sort()
  some_angles[1] = some_angles[2]
  some_angles[2] = 180 - some_angles[0] - some_angles[1] 

  ang_len_frame = pandas.DataFrame(anglength_dict)
  ang_len_frame = ang_len_frame.set_index('Angles')
  print(ang_len_frame)
  print()
  print("Please click on the green screen to continue")
  print()

  # Convert frames to strings
  ang_len_text = pandas.DataFrame.to_string(ang_len_frame)

  # export to file
  a_name = "Trig Answers"
  to_write = [a_name, ang_len_text, area, perimeter]

  # write to file...
  # Create file to hold data (add .txt extension)
  file_name = "{}.txt".format(a_name)
  text_file = open(file_name, "w+")

  # heading
  for item in to_write:
      text_file.write(item)
      text_file.write("\n\n")

  # close file
  text_file.close()
  draw = triangle(some_lengths, some_angles)
  keep_going = input("Press <ENTER> to repeat program or any other key to quit. ")
  some_angles.clear()
  some_lengths.clear()
print("Thank you for using this program and try to do your own trig homework")