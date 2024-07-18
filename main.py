from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()

# Separate the date and time
current_date = current_datetime.date()
current_time = current_datetime.time()


# Format the time to display only hours and minutes and current day
formatted_time = current_datetime.strftime("%H:%M:%S")

current_day = current_datetime.strftime("%A")
# Print the current date and time

print("The Current date:", current_date)
print("Current time:", formatted_time)
print("Today is:", current_day)
print('Automatic update change! This is cool!')