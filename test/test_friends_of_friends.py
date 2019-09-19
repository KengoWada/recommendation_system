import unittest
from recommendation.main import friends_of_friends
from test_base import graph


class TestFriendsOfFriends(unittest.TestCase):
    def test_friends_of_friends(self):
        """"Test if the correct friends of friends are returned"""
        self.assertEqual(friends_of_friends(graph, "A"), {"C", "E"})
        self.assertEqual(friends_of_friends(graph, "B"), {"D", "E", "G"})
        self.assertEqual(friends_of_friends(graph, "C"), {"A", "G", "F"})
        self.assertEqual(friends_of_friends(graph, "D"), {"B", "G", "F"})
        self.assertEqual(friends_of_friends(graph, "E"), {"A", "B"})
        self.assertEqual(friends_of_friends(graph, "F"), {"C", "D", "G"})
