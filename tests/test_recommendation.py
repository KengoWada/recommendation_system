import unittest

import networkx as nx

from recommendation import (
    common_friends,
    friends,
    friends_of_friends,
    influence_map,
    number_map_to_sorted_list,
    number_of_common_friends_map,
    recommend_by_influence,
    recommend_by_number_of_common_friends as rcf,
)

NODES = ["A", "B", "C", "D", "E", "F", "G"]

EDGES = [
    ("A", "B"),
    ("A", "G"),
    ("B", "C"),
    ("C", "D"),
    ("C", "E"),
    ("E", "D"),
    ("E", "F"),
    ("E", "G"),
]


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(NODES)
        self.graph.add_edges_from(EDGES)

    def test_common_friends_map(self):
        """Test if the correct common friends map is returned"""
        test_data = [
            {"input": "A", "output": {"C": 1, "E": 1}},
            {"input": "B", "output": {"D": 1, "G": 1, "E": 1}},
            {"input": "C", "output": {"G": 1, "F": 1, "A": 1}},
            {"input": "D", "output": {"G": 1, "F": 1, "B": 1}},
            {"input": "E", "output": {"A": 1, "B": 1}},
        ]
        for data in test_data:
            result = number_of_common_friends_map(self.graph, data["input"])
            self.assertEqual(result, data["output"])

    def test_common_friends(self):
        """ "Test if function returns correct common friends"""
        # Because the possible pairs out of the graph are many I will only test 3
        test_data = [
            {"input": ["B", "E"], "output": {"C"}},
            {"input": ["B", "G"], "output": {"A"}},
            {"input": ["D", "F"], "output": {"E"}},
        ]
        for data in test_data:
            result = common_friends(self.graph, *data["input"])
            self.assertEqual(result, data["output"])

    def test_friends_of_friends(self):
        """ "Test if the correct friends of friends are returned"""
        test_data = [
            {"input": "A", "output": {"C", "E"}},
            {"input": "B", "output": {"D", "E", "G"}},
            {"input": "C", "output": {"A", "G", "F"}},
            {"input": "D", "output": {"B", "G", "F"}},
            {"input": "E", "output": {"A", "B"}},
            {"input": "F", "output": {"C", "D", "G"}},
        ]
        for data in test_data:
            result = friends_of_friends(self.graph, data["input"])
            self.assertEqual(result, data["output"])

    def test_friends(self):
        """Test whether the friends function returns the correct output"""
        test_data = [
            {"input": "A", "output": {"B", "G"}},
            {"input": "B", "output": {"A", "C"}},
            {"input": "C", "output": {"B", "D", "E"}},
            {"input": "D", "output": {"C", "E"}},
            {"input": "E", "output": {"G", "F", "C", "D"}},
            {"input": "F", "output": {"E"}},
        ]
        for data in test_data:
            result = friends(self.graph, data["input"])
            self.assertEqual(result, data["output"])

    def test_influence_map(self):
        """ "Test influence map function is returning correct results"""
        self.assertEqual(influence_map(self.graph, "A"), {"E": 0.5, "C": 0.5})
        self.assertEqual(
            influence_map(self.graph, "B"), {"G": 0.5, "E": 1 / 3, "D": 1 / 3}
        )

    def test_influence_recommendation(self):
        """ "Test influence recommendation"""
        self.assertEqual(recommend_by_influence(self.graph, "A"), ["C", "E"])
        self.assertEqual(recommend_by_influence(self.graph, "B"), ["G", "D", "E"])

    def test_sort_map_to_list(self):
        """Test that the function sorts a dictionary and returns a list"""
        self.assertEqual(number_map_to_sorted_list({"A": 2, "H": 3}), ["H", "A"])

    def test_common_friend_recommendation(self):
        """Test common friend recommendation"""
        self.assertEqual(rcf(self.graph, "A"), ["C", "E"])
        self.assertEqual(rcf(self.graph, "E"), ["A", "B"])
