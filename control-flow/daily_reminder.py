# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a customized reminder using match-case and conditionals
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a HIGH priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a HIGH priority task. Complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a MEDIUM priority task that requires attention today.")
        else:
            print(f"\nReminder: '{task}' is a MEDIUM priority task. Try to schedule it soon.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a LOW priority task that requires immediate attention today!")
        else:
            print(f"\nNote: '{task}' is a LOW priority task. Consider doing it when you have free time.")
    case _:
        print("\nInvalid priority entered. Please enter 'high', 'medium', or 'low'.")

