import re
import random

patterns_responses = {
    r'hi|hello|hey': ['Hello!', 'Hi there!', 'Hey! How can I help you?'],
    r'how are you\?': ['I am fine, thank you!', 'I am doing well, how about you?'],
    r'what is your name\?': ['I am a chatbot created for you.', 'You can call me Chatbot.'],
    r'quit': ['Bye! Have a great day!', 'Goodbye!'],
}

def get_response(user_input):
    
    for pattern, responses in patterns_responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    
    return 'I am not sure I understand what you are saying. Could you please elaborate?'

def chat():
    print("Hi! I am your chatbot. Type 'quit' to end the conversation.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() == 'quit':
                print("Chatbot: Bye! Have a great day!")
                break
            response = get_response(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if _name_ == "_main_":
    chat()