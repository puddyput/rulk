from DialObserver.DialObserver import DialObserver


class TelephonyController(DialObserver):

    def notify(self, sequence: str):
        super().notify(sequence)
