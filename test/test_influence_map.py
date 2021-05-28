import unittest

from recommendation.main import influence_map

from .test_base import graph


class TestInfluenceMap(unittest.TestCase):
    def test_influence_map(self):
        """"Test influence map function is returning correct results"""
        self.assertEqual(influence_map(graph, "A"), {"E": 0.5, "C": 0.5})
        self.assertEqual(influence_map(graph, "B"), {
                         "G": 0.5, "E": 1/3, "D": 1/3})
