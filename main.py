from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()

# Separate the date and time
current_date = current_datetime.date()
current_time = current_datetime.time()

# Print the current date and time
print("Current date:", current_date)
print("Current time:", current_time)