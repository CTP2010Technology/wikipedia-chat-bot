from nlp_utils.nlp_utils import extract_entities, summarize_text
from wikipedia_utils.wikipedia_utils import safe_get_wikipedia_summary
from context_manager.context_manager import ChatbotContext

class Chatbot:
    def __init__(self):
        self.context = ChatbotContext()

    def handle_query(self, query):
        # Process the query
        entities = extract_entities(query)
        summary = safe_get_wikipedia_summary(query)
        self.context.add_to_history(query, summary)
        
        return {
            'entities': entities,
            'summary': summary
        }

    def get_context(self):
        return self.context.get_context()

    def clear_context(self):
        self.context.clear_context()
