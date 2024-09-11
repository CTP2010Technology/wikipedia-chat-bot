import logging

def setup_logging():
    logging.basicConfig(filename='chatbot.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

setup_logging()
