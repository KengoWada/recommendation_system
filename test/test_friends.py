import unittest

from recommendation.main import friends

from .test_base import graph


class TestFriends(unittest.TestCase):
    def test_friends(self):
        """
        Test whether the friends function returns the correct output
        """
        self.assertEqual(friends(graph, "A"), {"B", "G"})
        self.assertEqual(friends(graph, "B"), {"A", "C"})
        self.assertEqual(friends(graph, "C"), {"B", "D", "E"})
        self.assertEqual(friends(graph, "D"), {"C", "E"})
        self.assertEqual(friends(graph, "E"), {"G", "F", "C", "D"})
        self.assertEqual(friends(graph, "F"), {"E"})
