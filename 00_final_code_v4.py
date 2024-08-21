import pandas as pd
import re
from datetime import date


# Checks if the user has entered yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response in ["yes", "y"]:
            return "yes"

        elif response in ["no", "n"]:
            return "no"

        else:
            print("Please answer 'yes' or 'no'.")


# Shows instructions
def show_instructions():
    print('''\n
    ***** Instructions *****

    To Complete the BMX Competition Form Please Enter ...
    - The Team Name (This cannot include symbols, numbers or be left blank)
    - How Many Members Are In Your team (6 / 8)
    - How Many Races All Team Members Are Entered in (4/6)
    - Each Riders Name and Placings for chosen amount of races (1-4 / 1-6)
    - Repeat This Till All Riders Names and Placings have been entered
    
    Once all of the required information is collected...
    
    The program will display the team name and the date the form was also taken.
    
    The program will then display in a table with all the Riders Names,
    Each Riders Placing For Each race, Total Tally of Points Earned by each team Rider.
    
    
    This information will also be automatically written to 
    a text file.

    *****************************************\n''')


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
        elif re.search(r'[0-9!@#$%^&*()_+|}{:"?><]', response):
            print("Sorry, this section cannot be left blank and cannot contain numbers, symbols. Please "
                  "try again.")
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
if __name__ == '__main__':

    while True:

        # Check if user wants to continue with the form
        guide = enter_continue("Would you like to fill in a form for your BMX team? Press 'enter' to continue or 'xx' "
                               "to"
                               " exit: ")
        print()

        # If guide is False, exit the loop
        if not guide:
            print("Successfully Closed")
            break

        # Ask if the user wants to see the instructions
        instructions = yes_no("Would you like to see the instructions? 'yes' or 'no': ")

        if instructions == "yes":
            show_instructions()

        print()
        team_name = not_blank_no_integers_no_symbols("Enter your Team Name (or 'xx' to exit): ")

        if team_name == 'xx':
            print('Successfully Closed')
            break

        # Asking how many team members
        while True:
            print()
            num_team_members = num_check("Enter Number of Team Members (select '6' or '8'): ")
            if num_team_members in [6, 8]:
                print(f"Team {team_name} with {num_team_members} members is successfully registered.")
                break
            else:
                print("Sorry, this is an invalid option. Please select '6' or '8'.")

        # Asking how many races for every team member
        while True:
            print()
            num_races = num_check("Enter number of races ('4' or '6) for all team members: ")
            # Validate number of races
            if num_races in [4, 6]:
                print(f"You have selected {num_races} races for your team.")
                print()
                break
            else:
                print("Sorry, this is an invalid option. Please select '4' or '6'.")

        # Dictionary to hold all riders' data
        riders_data = {}
        # Calculate points and prepare DataFrame data
        data = {
            'Riders Name': [],
            **{f'Race {i + 1}': [] for i in range(num_races)},
            'Calculated Tally': []
        }

        # Loop to get each rider's information
        for i in range(num_team_members):
            print()
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
                            riders_data[rider_name].append(0)  # Or some placeholder value
                            print()
                            print("You have chosen not to compete in this race.")
                            break


                        else:
                            print()
                            print("Please enter a placing between 1 and 50.")
                    except ValueError:
                        print()
                        print("Invalid input. Please enter a placing between 1 and 50.")

        # Get current date for heading and file name
        today = date.today()

        # Format the date
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        heading = " ------------ BMX Riders Results ({}/{}/{}) ------------".format(day, month, year)
        filename = "BMX_File_{}_{}_{}".format(year, month, day)

        for rider_name, placings in riders_data.items():
            points = sum(calculate_points(p) for p in placings)
            data['Riders Name'].append(rider_name)
            for i in range(num_races):
                data[f'Race {i + 1}'].append(placings[i])
            data['Calculated Tally'].append(points)

        # Create the DataFrame
        df = pd.DataFrame(data)

        # Prepare the data to write to the file
        to_write = []
        to_write.append(heading)
        to_write.append(df.to_string(index=False))

        # Write output to file
        write_to = "{}.txt".format(filename)
        with open(write_to, "w+") as text_file:
            for item in to_write:
                text_file.write(item)
                text_file.write("\n")

        print()
        print(heading)
        print(f"*** Data has been written to {write_to} ***")

        # Display Team Name
        print(f"\n--------------------Team: {team_name}------------------------------")
        print(df.to_string(index=False))  # Display DataFrame without the index

        # Check if the user wants to process another team
        if not enter_continue("If you wish to exit press 'xx' or to continue with another team press 'enter': "):
            print('Successfully Closed')
            break
