import abc


class DialObserver(abc.ABC):

    @abc.abstractmethod
    def notify(self, sequence: str):
        pass
