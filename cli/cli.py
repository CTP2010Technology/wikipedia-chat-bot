from chatbot.core import Chatbot
from logging_config.logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

def main():
    chatbot = Chatbot()
    print("Welcome to the Advanced Wikipedia Chatbot!")
    print("Type 'exit' to quit.")
    while True:
        query = input("Enter a topic: ")
        if query.lower() == 'exit':
            break

        # Handle the query
        response = chatbot.handle_query(query)
        print("Entities detected:", response['entities'])
        print("Summary:", response['summary'])

        # Log the interaction
        logger.info(f"User query: {query}")
        logger.info(f"Chatbot response: {response['summary']}")

if __name__ == "__main__":
    main()
