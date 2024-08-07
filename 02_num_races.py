# Function to control continuation or exit of the program
def enter_continue(question):
    while True:
        response = input(question).strip().lower()
        if response == 'xx':
            return False
        elif response == "":
            return True
        else:
            print("Invalid input. Press 'enter' to continue or type 'xx' to exit.")


# Checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        else:
            return response


# Asking how many races for every team member
# Default is 4 races
while True:
    if not enter_continue("Press 'enter' to see race options (or type 'xx' to exit): "):
        break

    print("*** The default number of races is 4 ***")
    num_races = not_blank("Enter number of races (4 or 6): ")

    if num_races not in["4", "6"]:
        print("Invalid number of races. Defaulting to 4 races.")
        num_races = 4
    else:
        num_races = int(num_races)

    print(f"You have selected {num_races} races.")
