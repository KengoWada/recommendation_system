import networkx as nx

import unittest

nodes = ["A", "B", "C", "D", "E", "F", "G"]

edges = [("A", "B"), ("A", "G"), ("B", "C"), ("C", "D"),
         ("C", "E"), ("E", "D"), ("E", "F"), ("E", "G")]


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(nodes)
        self.graph.add_edges_from(edges)
