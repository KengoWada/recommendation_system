import unittest

from recommendation import common_friends

from .test_base import BaseTestCase


class TestCommonFriends(BaseTestCase):

    def test_common_friends(self):
        """"Test if function returns correct common friends"""
        # Because the possible pairs out of the graph are many I will only test 3
        self.assertEqual(common_friends(self.graph, "B", "E"), {"C"})
        self.assertEqual(common_friends(self.graph, "B", "G"), {"A"})
        self.assertEqual(common_friends(self.graph, "D", "F"), {"E"})
