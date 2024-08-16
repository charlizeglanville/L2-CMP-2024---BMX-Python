def calculate_points(placing):
    if placing == 1:
        return 5
    elif placing == 2:
        return 3
    elif placing == 3:
        return 1
    else:
        return 0


# For test purposes
rider_name = "Joesph"
num_races = 4  # For test purposes I will only have 4 races

total_points = 0  # Initialize total points

for i in range(num_races):
    while True:
        try:
            print("*** Enter 0 if you chose not to participate in a race or were disqualified *** ")
            placing = int(input(f"Enter the placing for {rider_name} in Race {i + 1} (1-50): "))
            print()
            if 1 <= placing <= 50:
                total_points += calculate_points(placing)  # Add points to total
                break

            if placing == 0:
                print("You have chosen not to compete in this race or you have been disqualified.")
                print()
                break

            else:
                print("Please enter a placing between 1 and 50.")
                print()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 50.")
            print()

print(f"Total points for {rider_name}: {total_points}")

