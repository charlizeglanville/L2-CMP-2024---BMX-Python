# Checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        else:
            return response


# Checks race number and number of team members
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")


# Function to handle continuation or exit
def enter_continue(question):
    while True:
        response = input(question).strip().lower()
        if response == 'xx':
            return False
        elif response == "":
            return True
        else:
            print("Invalid input. Press 'enter' to continue or type 'xx' to exit.")


# Loop to get Riders Information
while True:
    team_name = not_blank("Enter your Team Name(or 'xx' to exit): ")

    if team_name.lower() == 'xx':
        print('Successfully Closed')
        break

    # Check if user wants to continue or exit
    if not enter_continue("If you wish to exit press 'xx' or to continue press 'enter': "):
        print('Successfully Closed')
        break

    # Asking how many team members
    while True:
        num_team_members = num_check("Number of Team Members (select '6', or '8'): ")
        # Validate team members
        if num_team_members == 6 or num_team_members == 8:
            print(f"Team {team_name} with {num_team_members} members is successfully registered.")
            break  # Exit the inner loop if the number of team members is valid
        else:
            if 1 <= num_team_members <= 5 or num_team_members == 7:
                print("Sorry, this is an invalid option. Please select '6', or '8'.")
            elif num_team_members > 8:
                print("We don't currently have teams over 8 at this BMX competition.")
