import unittest
from chatbot.core import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_handle_query(self):
        response = self.chatbot.handle_query("Python (programming language)")
        self.assertIn('summary', response)
        self.assertIn('entities', response)

    def test_context_management(self):
        self.chatbot.handle_query("Python (programming language)")
        context = self.chatbot.get_context()
        self.assertGreater(len(context), 0)

        self.chatbot.clear_context()
        context = self.chatbot.get_context()
        self.assertEqual(len(context), 0)

if __name__ == '__main__':
    unittest.main()
