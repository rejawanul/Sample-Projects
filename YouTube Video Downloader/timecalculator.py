def time_calculator():
    try:
        # Get input from the user
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))

        # Calculate the total time in seconds
        total_seconds = hours * 3600 + minutes * 60 + seconds

        # Calculate hours, minutes, and remaining seconds
        calculated_hours, remainder = divmod(total_seconds, 3600)
        calculated_minutes, calculated_seconds = divmod(remainder, 60)

        # Display the result
        print(f"Total time: {calculated_hours} hours, {calculated_minutes} minutes, {calculated_seconds} seconds")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the time calculator function
time_calculator()