import unittest

from recommendation.main import number_of_common_friends_map

from .test_base import graph


class TestCommonFriendsMap(unittest.TestCase):
    def test_common_friends_map(self):
        """Test if the correct common friends map is returned"""
        self.assertEqual(number_of_common_friends_map(
            graph, "A"), {"C": 1, "E": 1})
        self.assertEqual(number_of_common_friends_map(
            graph, "B"), {"D": 1, "G": 1, "E": 1})
        self.assertEqual(number_of_common_friends_map(
            graph, "C"), {"G": 1, "F": 1, "A": 1})
        self.assertEqual(number_of_common_friends_map(
            graph, "D"), {"G": 1, "F": 1, "B": 1})
        self.assertEqual(number_of_common_friends_map(
            graph, "E"), {"A": 1, "B": 1})
