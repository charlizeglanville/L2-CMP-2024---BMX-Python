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


# Checks that user response is not blank and is an integer
def not_blank_num_check(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        else:
            try:
                response = int(response)
                return response
            except ValueError:
                print("Please enter an integer.")


# Asking how many races for every team member
# Default is 4 races
while True:
    if not enter_continue("Press 'enter' to see race options (or type 'xx' to exit): "):
        break

    # Asking user how many races each team is doing
    while True:
        num_races = not_blank_num_check("Enter number of races (4 or 6): ")
        # Validate number of races
        if num_races == 4 or num_races == 6:
            print(f"You have selected {num_races} races.")
            break  # Exit the inner loop if the number of races is valid
        else:
            print("Sorry, this is an invalid option. Please select '4' or '6'.")
