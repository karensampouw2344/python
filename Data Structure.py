# This program demonstrates the use of tuples, lists, and dictionaries in Python.

# Using a tuple to store fixed data
coordinates = (10, 20)

# Using a list to store a collection of names
names = ["Alice", "Bob", "Charlie"]

# Using a dictionary to associate student names with their grades
grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}

# Function to display the data
def display_data():
    print("Coordinates:", coordinates)
    print("Names:", names)
    print("Grades:")
    for name in names:
        print(f"{name}: {grades[name]}")

# Main function
if __name__ == "__main__":
    display_data()
