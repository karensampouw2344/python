def input_student_details ():
student_name = input ("Karen")
student_id = input ("2702217062")
gpa = float(input(3.0))
return {
    "Name" : student_name,
    "ID": student_id,
    "GPA": gpa
    
    }

if __name__ == "__main__":
    student_details = input_student_details()
    
    print("\nStudent Details:")
    print(f"Name: {student_details['Name']}")
    print(f"ID: {student_details['ID']}")
    print(f"GPA: {student_details['GPA']:.2f}")
    
num_odd = [0, 1, 3 ,5 ,7 ,9]
num_even = [2, 4, 6, 8, 10]
num = num_odd + num_even
print(num) # [0, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

100_zero = [0] * 100 # [0, 0, 0, 0, ...]

student = ["Albert", "Grace", "Charlie", "Tom"]

print(student[-1])      # Tom
print(student[-1::-1])  # ['Tom', 'Charlie', 'Grace', 'Albert']

numbers = [1, 2, 3, 4, 5]

first_number = numbers[0]  # 1
last_number = numbers[-1]   # 5

sublist = numbers[1:4]      # [2, 3, 4]

numbers.append(6)           # [1, 2, 3, 4, 5, 6]

numbers.insert(0, 0)        # [0, 1, 2, 3, 4, 5, 6]

numbers.remove(3)           # [0, 1, 2, 4, 5, 6]
popped_number = numbers.pop()  # Removes and returns the last element (6)

more_numbers = [7, 8, 9]
combined_list = numbers + more_numbers  # [0, 1, 2, 4, 5, 7, 8, 9]

print(f"First Number: {first_number}")
print(f"Last Number: {last_number}")
print(f"Sublist: {sublist}")
print(f"Updated List: {numbers}")
print(f"Popped Number: {popped_number}")
print(f"Combined List: {combined_list}")



# Function to calculate average score
def calculate_average(scores):
    if len(scores) == 0:
        return 0  # Avoid division by zero
    return sum(scores) / len(scores)

# Main function to execute the code
if __name__ == "__main__":
    # Input scores from the user
    scores = []
    num_scores = int(input("Enter the number of scores: "))
    
    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)
    
    # Calculate the average score
    average_score = calculate_average(scores)
    
    # Print the average score
    print(f"\nScores: {scores}")
    print(f"Average Score: {average_score:.2f}")
