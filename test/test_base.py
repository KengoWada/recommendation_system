import networkx as nx

nodes = ["A", "B", "C", "D", "E", "F", "G"]

edges = [("A", "B"), ("A", "G"), ("B", "C"), ("C", "D"),
         ("C", "E"), ("E", "D"), ("E", "F"), ("E", "G")]

graph = nx.Graph()

graph.add_nodes_from(nodes)
graph.add_edges_from(edges)
