from recommendation import friends

from .test_base import BaseTestCase


class TestFriends(BaseTestCase):

    def test_friends(self):
        """
        Test whether the friends function returns the correct output
        """
        self.assertEqual(friends(self.graph, "A"), {"B", "G"})
        self.assertEqual(friends(self.graph, "B"), {"A", "C"})
        self.assertEqual(friends(self.graph, "C"), {"B", "D", "E"})
        self.assertEqual(friends(self.graph, "D"), {"C", "E"})
        self.assertEqual(friends(self.graph, "E"), {"G", "F", "C", "D"})
        self.assertEqual(friends(self.graph, "F"), {"E"})
