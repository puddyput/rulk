from Observer import Observer


class Menu:
    sequence = ""
    observer = {}

    def key_event(self, key: str):
        self.sequence += key
        self.notify()

    def register(self, prefix: str, observer: Observer):
        self.observer[prefix] = observer

    def notify(self):
        for prefix, observer in self.observer.items():
            if self.sequence.startswith(prefix):
                observer.notify(self.sequence)