# import statements

# functions go here
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print("Sorry - this can't be blank. " "Please enter your name")

# ***** Main routine *****

# Set up dictionaries / lists needed to hold data

# Ask user if they used the programme before and show instructions if necessary

# Loop to get ticket details

  # Get name (can't be blank)

  # Get age (between 12 and 130)

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count <= MAX_TICKETS:
  print("You have {} seats "
        "left".format(MAX_TICKETS - count))

  name = not_blank("Name: ")
  count += 1
  print()

if count == MAX_TICKETS:
  print("You have sold all the available tickets!")
else:
  print("You have sold {} tickets. \n"
       "There are {} places still available"
       .format(count, MAX_TICKETS - count))

  # Calculate ticket price

  # Loop to ask for snacks

  # Calculate snack price

# Ask for payment method (and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file