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

def int_check(question, low_num, high_num):
  error = "Please enter a whole number between {} " \
          "and {}".format(low_num, high_num)
  valid = False
  while not valid:
    try:
      response = int(input(question))
      return response
    except ValueError:
      print(error)

def string_check(choice, options):
  for var_list in options:
    if choice in var_list:
      chosen = var_list[0].title()
      is_valid = "yes"
      break
    else:
      is_valid = "no"
  if is_valid == "yes":
    return chosen
  else:
    return "invalid choice"
# ***** Main routine *****

# Set up dictionaries / lists needed to hold data

# Ask user if they used the programme before and show instructions if necessary

# Loop to get ticket details

  # Get name (can't be blank)

name = ""
ticket_count = 0
MAX_TICKETS = 5
profit = 0
ticket_sales = 0

while name != "xxx" and ticket_count < MAX_TICKETS:
  if ticket_count < 4:
    print()
    print("You have {} seats "
         "left".format(MAX_TICKETS - ticket_count))
    age = int_check("Age: ", 12, 130)

  else:
    print("*** There is ONE seat left!! ***")
    age = int_check("Age: ", 12, 130)

  name = not_blank("Name: ")
  ticket_count += 1
  print()
  if age < 16:
    ticket_price = 7.5
  elif age < 65:
    ticket_price = 10.5
  else:
    ticket_price = 6.5

  profit_made = ticket_price - 5
  profit += profit_made
  print("{} : ${:.2f}".format(name, ticket_price))
  ticket_sales += ticket_price

  if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
    print("Profit from Tickets: ${:.2f}".format(profit))
  else:
    print("You have sold {} tickets. \n"
       "There are {} places still available"
       .format(ticket_count, MAX_TICKETS - ticket_count))

  valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
  ]

  yes_no = [
    ["yes", "y"],
    ["no", "n"]
  ]

  snack_order = []

  check_snack = "invalid choice"
  while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    print()
    print("KEY: Type 'xxx' if you have finished ordering")
    check_snack = string_check(want_snack, yes_no)
  if check_snack == "Yes":
    desired_snack = ""
    while desired_snack != "xxx":
      desired_snack = input("Snack: ").lower()
      if desired_snack == "xxx":
        break
      snack_choice = string_check(desired_snack, valid_snacks)
      print("Snack Choice: ", snack_choice)
      if snack_choice != "xxx" and snack_choice != "invalid choice":
        snack_order.append(snack_choice)

  print()
  if len(snack_order) == 0:
    print("Snacks Ordered: None")
  else:
    print("Snacks Ordered:")
    for item in snack_order:
      print(item)

  # Get age (between 12 and 130)

  # Calculate ticket price

  # Loop to ask for snacks

  # Calculate snack price

# Ask for payment method (and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file