# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response == "" or response == " ":
            print("Sorry, this can't be blank. Please try again")
        else:
            return response


while True:
    name = not_blank("Enter your name (or exit using 'xx'): ")
    # Exit Loop if users type 'xx'
    if name == 'xx':
        print()
        print('Successfully Closed')
        break
    else:
        continue
