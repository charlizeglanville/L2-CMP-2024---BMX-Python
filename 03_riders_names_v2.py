import re


# Checks that user response is not blank and does not contain integers or symbols
def not_blank_no_integers_no_symbols(question):
    while True:
        response = input(question).strip()
        if not response:
            print("Sorry, this can't be blank. Please try again.")
        elif re.search(r'[0-9!@#$%^&*()_+|}{:"?><]', response): # re search searches for regular string that matches a regular expression
            print("Sorry, the input cannot contain numbers or symbols. Please try again.")
        else:
            return response


num_team_members = 6
num_races = 4

# Dictionary to hold all riders' data
riders_data = {}

# Loop to get each rider's information
for i in range(num_team_members):
    rider_name = not_blank_no_integers_no_symbols(f"Enter the name of rider {i + 1}: ")
