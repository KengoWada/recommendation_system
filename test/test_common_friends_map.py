import unittest

from recommendation import number_of_common_friends_map


from .test_base import BaseTestCase


class TestCommonFriendsMap(BaseTestCase):

    def test_common_friends_map(self):
        """Test if the correct common friends map is returned"""
        self.assertEqual(number_of_common_friends_map(
            self.graph, "A"), {"C": 1, "E": 1})
        self.assertEqual(number_of_common_friends_map(
            self.graph, "B"), {"D": 1, "G": 1, "E": 1})
        self.assertEqual(number_of_common_friends_map(
            self.graph, "C"), {"G": 1, "F": 1, "A": 1})
        self.assertEqual(number_of_common_friends_map(
            self.graph, "D"), {"G": 1, "F": 1, "B": 1})
        self.assertEqual(number_of_common_friends_map(
            self.graph, "E"), {"A": 1, "B": 1})
