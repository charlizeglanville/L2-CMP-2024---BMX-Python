import pandas as pd
import re


# Checks race number and number of team members
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")


# Checks that user response is not blank and does not contain integers or symbols
def not_blank_no_integers_no_symbols(question):
    while True:
        response = input(question).strip()
        if not response:
            print("Sorry, this can't be blank. Please try again.")
        elif re.search(r'[0-9!@#$%^&*()_+|}{:"?><]',
                       response):  # re search searches for regular string that matches a regular expression
            print("Sorry, the input cannot contain numbers or symbols. Please try again.")
        else:
            return response


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


# Function to calculate points based on placing
def calculate_points(placing):
    if placing == 1:
        return 5
    elif placing == 2:
        return 3
    elif placing == 3:
        return 1
    else:
        return 0


# Main program loop
while True:
    team_name = not_blank_no_integers_no_symbols("Enter your Team Name (or 'xx' to exit): ")

    if team_name.lower() == 'xx':
        print('Successfully Closed')
        break

    # Check if user wants to continue or exit
    if not enter_continue("If you wish to exit press 'xx' or to continue press 'enter': "):
        print('Successfully Closed')
        break

    # Asking how many team members
    while True:
        print()
        num_team_members = num_check("Number of Team Members (select '6' or '8'): ")
        if num_team_members in [6, 8]:
            print(f"Team {team_name} with {num_team_members} members is successfully registered.")
            break
        else:
            print("Sorry, this is an invalid option. Please select '6' or '8'.")

    # Asking how many races for every team member
    while True:
        print()
        num_races = num_check("Enter number of races (4 or 6) for all team members: ")
        # Validate number of races
        if num_races in [4, 6]:
            print(f"You have selected {num_races} races for your team.")
            print()
            break
        else:
            print("Sorry, this is an invalid option. Please select '4' or '6'.")

    # Dictionary to hold all riders' data
    riders_data = {}

    # Loop to get each rider's information
    for i in range(num_team_members):
        rider_name = not_blank_no_integers_no_symbols(f"Enter the name of rider {i + 1}: ")
        riders_data[rider_name] = []
        print()
        for j in range(num_races):
            while True:
                try:
                    placing = int(input(f"Enter the placing for {rider_name} in Race {j + 1} (1-50): "))
                    if 1 <= placing <= 50:
                        riders_data[rider_name].append(placing)
                        break

                    if placing == 0:
                        print("You have chosen not to compete in this race.")
                        break

                    else:
                        print("Please enter a placing between 1 and 50.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 50.")

    # Calculate points and prepare DataFrame data
    data = {
        'Riders Name': [],
        **{f'Race {i + 1}': [] for i in range(num_races)},
        'Total Points': []
    }

    for rider_name, placings in riders_data.items():
        points = sum(calculate_points(p) for p in placings)
        data['Riders Name'].append(rider_name)
        for i in range(num_races):
            data[f'Race {i + 1}'].append(placings[i])
        data['Total Points'].append(points)

    # Create the DataFrame
    df = pd.DataFrame(data)

    # Display DataFrame
    print(f"\nTeam: {team_name}")
    print(df)

    # Check if the user wants to process another team / gives the option to the user to enter another team
    if not enter_continue("If you wish to exit press 'xx' or to continue with another team press 'enter': "):
        print('Successfully Closed')
        break
