# checks that there are no numbers in the string for user input
def shape():
  error = "Please enter a valid shape"
 
  while True:
    has_number = False
    polygon = input("What is the shape you are trying to solve for? ")

    for i in polygon:
      if i.isdigit():
        has_number = True
        
    if has_number == True:
      print(error)

    else:
      return polygon

appearance = shape()


        