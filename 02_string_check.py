# checks that there are no numbers in the string for user input
def num_check(question, low, high, type):
  error = "Please enter a number more than {} or less than {}".format(high, low)

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

what_to_do = string_checker("Proceed? ", ["yes", "no"])
  
  
  




        