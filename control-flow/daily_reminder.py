# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Construct the base reminder message
match priority:
    case "high" | "medium" | "low":
        reminder = f"Reminder: '{task}' is a {priority.upper()} priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Plan accordingly based on your schedule."
        print("\n" + reminder)
    case _:
        print("\nInvalid priority entered. Please enter 'high', 'medium', or 'low'.")

