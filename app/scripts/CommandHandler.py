
from .widgets.NewsWidget import NewsWidget
from .agent.classes.Voice import Voice

sample = "Alexa, tell me a little about the news"

# Class to manage all voice requests and return command information to socket connection
class CommandHandler:

    voice = Voice()  # Voice module from voice-agent repository

    commands = {
        'news': NewsWidget(),
        'close': "yeet",
    }

    def __init__(self):
        pass

    # Input text, return which key to execute
    def __search_for_key(self, text):
        for key in self.commands:
            if key in text:
                return key

    def run(self, text):
        key = self.__search_for_key(text)
        if (key == "close"):
            return {'close': key, 'data': "none"}
        self.script = self.commands[key].get_script()
        return {'open': "news", 'data': self.commands[key].get()}

    def speak(self):
        self.voice.say(self.script)

