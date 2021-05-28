import math

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


def find_side():
  degree = num_check("How many degrees? ", 0, 180, int)

  radian = degree * (math.pi/180)
  return radian


for item in range(0, 3):
  length = find_side()
  print(length)
  theta = math.sin(length)
  
# convert radians to degrees
# radians * 180/pi
# convert to degrees
# degrees * pi/180 