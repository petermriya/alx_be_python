from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

def main():
    current_time = display_current_datetime()
    print("Current date and time:", current_time)
    days = int(input("Enter number of days: "))
    future_date = calculate_future_date(days)
    print("Future date:", future_date)

if __name__ == "__main__":
    main()