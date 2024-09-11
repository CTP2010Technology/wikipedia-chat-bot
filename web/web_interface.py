from flask import Flask, request, jsonify
from chatbot.core import Chatbot
from logging_config.logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/get_fact', methods=['GET'])
def get_fact():
    topic = request.args.get('topic')
    if not topic:
        return jsonify({"error": "No topic provided."}), 400

    response = chatbot.handle_query(topic)
    logger.info(f"Received request for topic: {topic}")
    return jsonify({
        'entities': response['entities'],
        'summary': response['summary']
    })

@app.route('/context', methods=['GET'])
def get_context():
    context = chatbot.get_context()
    return jsonify({'context': context})

@app.route('/clear_context', methods=['POST'])
def clear_context():
    chatbot.clear_context()
    return jsonify({"message": "Context cleared."})

if __name__ == '__main__':
    app.run(debug=True)
