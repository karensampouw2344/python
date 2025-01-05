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