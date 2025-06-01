# pattern_drawing.py

# Prompt the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to handle rows
while row < size:
    # For loop to print asterisks in a row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    # Increment row counter
    row += 1
