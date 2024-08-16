def calculate_points(placing):
    if placing == 1:
        return 5
    elif placing == 2:
        return 3
    elif placing == 3:
        return 1
    else:
        return 0

total_points = 0

while True:
    try:
        placing = int(input("What is your placing (1-50): "))
        if 1 <= placing <= 50:
            points = calculate_points(placing)
            print(f"Total points: {points}")
        if placing == 0:
            print("You chose not to enter the race.")
            break
        else:
            print("Please enter a placing between 1 and 50.")
    except ValueError:
        print("Invalid input. Please enter a number.")
