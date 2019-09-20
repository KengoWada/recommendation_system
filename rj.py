from recommendation.main import recommend_by_number_of_common_friends as rcf
from recommendation.main import recommend_by_influence as rif
import networkx as nx
import random

characters = ["Nurse", "Juliet", "Capulet", "Tybalt", "Friar Laurence",
              "Romeo", "Benvolio", "Montague", "Escalus", "Mercutio", "Paris"]

relationships = [("Nurse", "Juliet"), ("Juliet", "Tybalt"), ("Juliet", "Friar Laurence"),
                 ("Juliet", "Romeo"), ("Juliet", "Capulet"), ("Capulet", "Tybalt"),
                 ("Capulet", "Escalus"), ("Capulet",
                                          "Paris"), ("Romeo", "Friar Laurence"),
                 ("Romeo", "Benvolio"), ("Romeo",
                                         "Montague"), ("Romeo", "Mercutio"),
                 ("Benvolio", "Montague"), ("Montague",
                                            "Escalus"), ("Escalus", "Mercutio"),
                 ("Escalus", "Paris"), ("Mercutio", "Paris")]

rj = nx.Graph()

rj.add_nodes_from(characters)
rj.add_edges_from(relationships)

same = 0
different = 0

f = open("results/rj_algorithm_diff.txt", "w")

for character in characters:
    if rcf(rj, character) == rif(rj, character):
        same += 1
        f.write("Same\n")
    else:
        different += 1
        f.write("Different\n")

f.write("\n")
f.write("Same: " + str(same) + "\n")
f.write("Different: " + str(different) + "\n")

f.close()


def compare_algorithms(graph, edges):
    # Select a random relationship and remove it from the graph
    edge = random.choice(edges)
    graph.remove_edge(edge[0], edge[1])
    user1 = edge[0]
    user2 = edge[1]

    # Recommendation by common friends
    user1_common_recommendations = rcf(graph, user1)
    user2_common_recommendations = rcf(graph, user2)

    if user1 in user2_common_recommendations and user2 in user1_common_recommendations:
        user1_common_rank = user2_common_recommendations.index(user1) + 1
        user2_common_rank = user1_common_recommendations.index(user2) + 1
        common_average = (user1_common_rank + user2_common_rank) / 2
    else:
        graph.add_edge(user1, user2)
        return 0

    # Recommendation by influence
    user1_influence_recommendations = rif(graph, user1)
    user2_influence_recommendations = rif(graph, user2)

    if user1 in user2_influence_recommendations and user2 in user1_influence_recommendations:
        user1_influence_rank = user2_influence_recommendations.index(user1) + 1
        user2_influence_rank = user1_influence_recommendations.index(user2) + 1
        influence_average = (user1_influence_rank + user2_influence_rank) / 2
    else:
        graph.add_edge(user1, user2)
        return 0

    # Add the relationship back to the graph
    graph.add_edge(user1, user2)

    # Compare results
    better = ""

    algorithm_analysis.write(
        "Average rank influence algorithm: " + str(influence_average) + "\n")
    algorithm_analysis.write(
        "Average rank common friends algorithm: " + str(common_average) + "\n")
    if common_average < influence_average:
        better = "common"
        algorithm_analysis.write("Common friends algorithm is better\n")
    elif influence_average < common_average:
        better = "influence"
        algorithm_analysis.write("Influence algorithm is better\n")
    else:
        better = "none"
        algorithm_analysis.write("None is better\n")

    algorithm_analysis.write("\n")

    return better


algorithm_analysis = open("results/rj_algorithm_analysis.txt", "w")

common = 0
influence = 0
none = 0

for i in range(1, 101):
    better = compare_algorithms(rj, relationships)
    if better == "common":
        common += 1
    elif better == "influence":
        influence += 1
    else:
        none += 1

algorithm_analysis.write("Common algorithm: " + str(common) + "\n")
algorithm_analysis.write("Influence algorithm: " + str(influence) + "\n")
algorithm_analysis.write("Neutral: " + str(none) + "\n")


algorithm_analysis.close()
