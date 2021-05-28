from recommendation import recommend_by_influence

from .test_base import BaseTestCase


class TestInfluenceRecommendation(BaseTestCase):

    def test_influence_recommendation(self):
        """"Test influence recommendation"""
        self.assertEqual(recommend_by_influence(self.graph, "A"), ["C", "E"])
        self.assertEqual(recommend_by_influence(
            self.graph, "B"), ["G", "D", "E"])
