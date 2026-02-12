# Basic Chatbot - CodeAlpha Internship Task 4

print("🤖 Chatbot: Hello! I am your chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Chatbot: Hi! Nice to meet you.")
    
    elif user == "how are you":
        print("Chatbot: I am fine, thanks! How can I help you?")
    
    elif user == "your name":
        print("Chatbot: I am CodeAlpha Chatbot.")
    
    elif user == "help":
        print("Chatbot: I can respond to hello, how are you, and bye.")
    
    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    
    else:
        print("Chatbot: Sorry, I don't understand that.")
