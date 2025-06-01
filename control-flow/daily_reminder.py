# daily_reminder.py

# Get task details from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = f"'{task}' is a {priority} priority task"

# Process priority using Match Case
match priority:
    case "high":
        reminder += " that should be addressed promptly"
    case "medium":
        reminder += " that can be handled when convenient"
    case "low":
        reminder += ". Consider completing it when you have free time"
    case _:
        reminder = f"'{task}' has an invalid priority. Please use high, medium, or low"
        print(reminder)
        exit()

# Check time sensitivity and modify reminder if needed
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    if priority != "low":  # Only append for non-low priority to avoid redundancy
        reminder += "."
else:
    reminder = f"Invalid input for time-bound. Please use yes or no."
    print(reminder)
    exit()

# Print final reminder with a simple loop for emphasis
print("\n" + "*" * 50)
for _ in range(1):  # Single iteration to keep it simple
    print(f"Reminder: {reminder}")
print("*" * 50)

