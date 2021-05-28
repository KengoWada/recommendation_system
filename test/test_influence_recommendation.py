import unittest

from recommendation.main import recommend_by_influence

from .test_base import graph


class TestInfluenceRecommendation(unittest.TestCase):
    def test_influence_recommendation(self):
        """"Test influence recommendation"""
        self.assertEqual(recommend_by_influence(graph, "A"), ["C", "E"])
        self.assertEqual(recommend_by_influence(graph, "B"), ["G", "D", "E"])
