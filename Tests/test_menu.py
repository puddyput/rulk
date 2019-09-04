from unittest import TestCase

from DialObserver.DialObserver import DialObserver
from Menu import Menu


class DummyDialObserver(DialObserver):
    lastSequence = ""

    def notify(self, sequence: str):
        self.lastSequence = sequence


class TestMenu(TestCase):
    def test_notify(self):
        menu = Menu()
        o = DummyDialObserver()
        menu.register("00", o)
        menu.key_event("0")
        self.assertEqual("", o.lastSequence)
        menu.key_event("0")
        self.assertEqual("00", o.lastSequence)
        menu.key_event("6")
        self.assertEqual("006", o.lastSequence)
