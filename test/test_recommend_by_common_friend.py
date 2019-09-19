import unittest
from recommendation.main import recommend_by_number_of_common_friends as rcf
from test_base import graph


class TestCommonFriendRecommendation(unittest.TestCase):
    def test_common_friend_recommendation(self):
        """Test common friend recommendation"""
        self.assertEqual(rcf(graph, "A"), [])
        self.assertEqual(rcf(graph, "E"), ["C", "D"])
