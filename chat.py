# chat.py

class ChatBot:
    def __init__(self, engine):
        self.engine = engine

    def alert(self, message):
        """Speak out the alert message."""
        self.engine.say(message)
        self.engine.runAndWait()

    def update_user(self, update_info):
        """Notify the user about updates."""
        self.alert(update_info)
