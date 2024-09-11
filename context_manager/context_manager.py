class ChatbotContext:
    def __init__(self):
        self.history = []

    def add_to_history(self, user_input, bot_response):
        self.history.append((user_input, bot_response))

    def get_context(self):
        return self.history

    def clear_context(self):
        self.history = []
