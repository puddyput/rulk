from unittest import TestCase

from TextToSpeech.TTLEngine import TTLEngine


class TestTTLEngine(TestCase):
    def test_say(self):
        ttl = TTLEngine()
        ttl.say("laber"*3)
