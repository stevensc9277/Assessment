import pandas
# Ask user for lengths and angles

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


some_angles = []
some_lengths = []

for i in range(0, 3):
  angles = num_check("How many degrees? ", 0, 180, int)
  lengths = num_check("How long? ", 0, 100, float)
  some_angles.append(angles)
  some_lengths.append(lengths)

anglength_dict = {
  'Angles': some_angles,
  'Lengths': some_lengths
}
frame = pandas.DataFrame(anglength_dict)
print(frame)