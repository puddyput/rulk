import pyttsx3
from threading import Thread


class TTLEngine:
    _engine = None

    def __init__(self):
        self._engine = pyttsx3.init()
        self._engine.setProperty("voice", "german")
        self._engine.setProperty("rate", 100)

    def say(self, text: str) -> None:
        t = Thread(target=self._engine.say, args=text)
        t.start()
