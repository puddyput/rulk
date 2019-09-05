import subprocess

from DialObserver.DialObserver import DialObserver
from Menu.Menu import Menu


class TelephonyController(DialObserver):

    def notify(self, sequence: str):
        last_input = sequence[-1]

        if last_input == Menu.KEY_PICKUP:
            self.start_call(sequence[0:-1])

        if last_input == Menu.KEY_HANGUP:
            self.stop_call()

    def start_call(self, number: str) -> None:
        subprocess.run(["screen", "-S", "rulk_twinkle", "-p", "0", "-X", "stuff", "bye^Mcall {}^M".format(number)])

    def stop_call(self):
        subprocess.run(["screen", "-S", "rulk_twinkle", "-p", "0", "-X", "stuff", "bye^M"])
