# Define a function to handle user input
def chatbot_response(user_input):
    # Convert user input to lower case for case insensitive matching
    user_input = user_input.lower()

    # Rule-based responses
    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! Thanks for asking."
    elif "weather" in user_input:
        return "The weather today is sunny with a slight chance of rain."
    elif "whats your name" or "your name" in user_input:
        return "I don't have any name.I am a chatbot"
    elif "goodbye" or "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase?"

# conversations
while True:
    
    user_input = input("u 😎:-")

    response = chatbot_response(user_input)
    
    print("Chatbot: " + response)

    # End of conversation 
    if "goodbye" or "bye" in user_input:
        break
