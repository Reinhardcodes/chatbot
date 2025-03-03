
import json
import os

class SmartChatbot:
    def __init__(self, data_file='chatbot_data.txt'):
        self.data_file = data_file
        self.responses = {}
        self.load_responses()

    def load_responses(self):
        """Load responses from the data file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.responses = json.load(file)
        else:
            self.responses = {}

    def save_responses(self):
        """Save responses to the data file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.responses, file)

    def train(self):
        """Train the chatbot with a new question and response."""
        question = input("Enter a question: ")
        response = input("Enter the response: ")
        self.responses[question] = response
        self.save_responses()
        print("Training complete!")

    def chat(self):
        """Chat with the user using predefined and learned responses."""
        print("Chatbot is ready to chat! Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            # Use a lambda function to get the response
            response = (lambda q: self.responses.get(q, "I'm sorry, I don't understand that."))(user_input)
            print("Chatbot:", response)

    def menu(self):
        """Display the menu and handle user choices."""
        while True:
            print("\nMenu:")
            print("1. Train the chatbot")
            print("2. Chat with the chatbot")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")

            if choice == '1':
                self.train()
            elif choice == '2':
                self.chat()
            elif choice == '3':
                print("Exiting the chatbot. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    chatbot = SmartChatbot()
    chatbot.menu()