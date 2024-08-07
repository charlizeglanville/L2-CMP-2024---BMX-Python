
# Checks that user response is not blank
def not_blank_and_no_integers(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        elif any(char.isdigit() for char in response): # checks for any digits and integers.
            print("Sorry, the input cannot contain numbers. Please try again.")
        else:
            return response


num_team_members = 6
num_races = 4

# Dictionary to hold all riders' data
riders_data = {}

# Loop to get each rider's information
for i in range(num_team_members):
    rider_name = not_blank_and_no_integers(f"Enter the name of rider {i + 1}: ")
