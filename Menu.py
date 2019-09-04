from DialObserver import DialObserver


class Menu:
    KEY_PICKUP = "P"
    KEY_HANGUP = "H"
    KEY_BUTTON_A = "A"

    _sequence = ""
    _observer = {}

    def key_event(self, key: str):
        self._sequence += key
        self.notify()

    def register(self, prefix: str, observer: DialObserver):
        self._observer[prefix] = observer

    def notify(self):
        for prefix, observer in self._observer.items():
            if self._sequence.startswith(prefix):
                observer.notify(self._sequence)
