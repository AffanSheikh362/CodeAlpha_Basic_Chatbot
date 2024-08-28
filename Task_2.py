import nltk
import random
import string
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample responses
greeting_responses = ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you today?"]
goodbye_responses = ["Goodbye!", "See you later!", "Bye! Take care!", "It was nice talking to you!"]

# Chatbot's response templates
def chatbot_response(user_input):
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]
    
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return random.choice(greeting_responses)
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return random.choice(goodbye_responses)
    else:
        return generate_response(user_input)

def generate_response(user_input):
    # Simple rule-based response generator


    
    if 'your name' in user_input:
        return "I'm a chatbot created by Affan. What's your name?"
    elif 'how are you' in user_input:
        return "I'm just a bunch of code, but I'm doing great! How about you?"
    elif 'what can you do' in user_input:
        return "I can chat with you, answer questions, and keep you company. What would you like to talk about?"
    elif 'age' in user_input:
        return "Age is just a number! Especially for a chatbot like me."
    elif 'food' in user_input:
        return "I don't eat, but if I could, I'd probably love pizza. How about you?"
    elif 'place' in user_input:
        return "I exist in the digital world, but I think the world outside is fascinating!"
    else:
        return "I'm not sure how to respond to that. Could you ask something else?"






# Main chat loop
def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot created by 'AFFAN'. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot:", random.choice(goodbye_responses))
            break
        else:
            print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    chatbot()
