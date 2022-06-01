def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print("Sorry - this can't be blank. " "Please enter your name")


name = not_blank("Name: ")
