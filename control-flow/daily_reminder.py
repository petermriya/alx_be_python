# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide customized reminder using match-case and conditionals
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Make sure to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that still needs attention today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Schedule it accordingly.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task, but it is time-bound. Try to do it today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority entered. Please enter high, medium, or low.")

