import math

# Checks that user input (number) is valid 
def num_check(question, low, high, type):
  error = "Please enter a number more than {} or less than {}".format(low, high)

  while True:
    try:
      response = type(input(question))

      if response <= 0:
        print(error)
        print()
      
      elif response >= 180:
        print(error)
        print()
      else:
        return response
    
    except ValueError:
      print(error)
      print()

side_a = num_check("How long? ", 0, 1000, float)
side_b = num_check("How long? ", 0, 1000, float)
inc_angle = num_check("What is the inclusive angle? ", 0, 150, float)
height = side_b*math.sin(math.radians(inc_angle))
area = 0.5 * height * side_a
print("Area = {:.2f}cm^2".format(area))