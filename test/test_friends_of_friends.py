from recommendation import friends_of_friends

from .test_base import BaseTestCase


class TestFriendsOfFriends(BaseTestCase):

    def test_friends_of_friends(self):
        """"Test if the correct friends of friends are returned"""
        self.assertEqual(friends_of_friends(self.graph, "A"), {"C", "E"})
        self.assertEqual(friends_of_friends(self.graph, "B"), {"D", "E", "G"})
        self.assertEqual(friends_of_friends(self.graph, "C"), {"A", "G", "F"})
        self.assertEqual(friends_of_friends(self.graph, "D"), {"B", "G", "F"})
        self.assertEqual(friends_of_friends(self.graph, "E"), {"A", "B"})
        self.assertEqual(friends_of_friends(self.graph, "F"), {"C", "D", "G"})
