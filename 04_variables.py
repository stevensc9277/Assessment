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


def how_many(question, length_or_deg):
  global some_angles
  global some_lengths
  repeats = num_check(question, 0, 3, int)
  for item in range(0, repeats): 
    if length_or_deg[0] == "l":
      angles_length = num_check("How long? ", 0, 150, int)
      some_lengths.append(angles_length)
    
    else:
      angles_length = num_check("How many degrees? ", 0, 150, int)
      some_angles.append(angles_length)

   

some_angles = []
some_lengths = []

angles = how_many("How many angles do you know? ", "degrees")
print()
lengths = how_many("How many lengths do you know? ", "long")


if len(some_angles) < len(some_lengths):
  some_angles.append(0)

elif len(some_lengths) < len(some_angles):
  some_lengths.append(0)


anglength_dict = {
  'Angles': some_angles,
  'Lengths': some_lengths
}

print()
frame = pandas.DataFrame(anglength_dict)
frame = frame.set_index('Angles')
print(frame)
print("Total angles: ",sum(some_angles))