# Checks that user input (number) is valid 

def num_check(question, low, high, type):
  error = "Please enter a number more than {} or less than {}".format(high, low)

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

# test
side_a = num_check("Enter a length: ", 1, 180, float)
print(side_a)