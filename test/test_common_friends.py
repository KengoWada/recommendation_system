import unittest

from recommendation.main import common_friends

from .test_base import graph


class TestCommonFriends(unittest.TestCase):
    def test_common_friends(self):
        """"Test if function returns correct common friends"""
        # Because the possible pairs out of the graph are many I will only test 3
        self.assertEqual(common_friends(graph, "B", "E"), {"C"})
        self.assertEqual(common_friends(graph, "B", "G"), {"A"})
        self.assertEqual(common_friends(graph, "D", "F"), {"E"})
