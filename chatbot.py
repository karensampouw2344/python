import random

# Define a function to handle the chatbot's responses
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    # Define a dictionary of possible responses based on user input
    responses = {
        "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
        "hello": ["Hi!", "Hello! How's it going?", "Hey, what's up?"],
        "how are you": ["I'm doing great, thanks for asking!", "I'm good, how about you?", "I'm fine, thank you!"],
        "bye": ["Goodbye!", "See you later!", "Bye, have a nice day!"],
        "default": ["Sorry, I didn't understand that.", "Can you rephrase that?", "I don't know how to respond to that."]
    }

    # Check if the user input matches any of the predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # Default response if no match is found
    return random.choice(responses["default"])

# Main function to interact with the user
def chat():
    print("Chatbot: Hello! I am a basic chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response)

# Start the chatbot
if __name__ == "__main__":
    chat()
