import unittest
from recommendation.main import number_of_common_friends_map
from test_base import graph


class TestCommonFriendsMap(unittest.TestCase):
    def test_common_friends_map(self):
        """Test if the correct common friends map is returned"""
        self.assertEqual(number_of_common_friends_map(graph, "A"), {})
        self.assertEqual(number_of_common_friends_map(graph, "B"), {})
        self.assertEqual(number_of_common_friends_map(
            graph, "C"), {"D": 1, "E": 1})
        self.assertEqual(number_of_common_friends_map(
            graph, "D"), {"C": 1, "E": 1})
        self.assertEqual(number_of_common_friends_map(
            graph, "E"), {"C": 1, "D": 1})
