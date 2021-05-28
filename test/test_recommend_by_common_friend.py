from recommendation import recommend_by_number_of_common_friends as rcf

from .test_base import BaseTestCase


class TestCommonFriendRecommendation(BaseTestCase):
    def test_common_friend_recommendation(self):
        """Test common friend recommendation"""
        self.assertEqual(rcf(self.graph, "A"), ["C", "E"])
        self.assertEqual(rcf(self.graph, "E"), ["A", "B"])
