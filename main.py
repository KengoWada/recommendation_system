import random

import networkx as nx

from recommendation import recommend_by_influence as rif
from recommendation import recommend_by_number_of_common_friends as rcf

CHARACTERS = [
    "Nurse",
    "Juliet",
    "Capulet",
    "Tybalt",
    "Friar Laurence",
    "Romeo",
    "Benvolio",
    "Montague",
    "Escalus",
    "Mercutio",
    "Paris",
]

RELATIONSHIPS = [
    ("Nurse", "Juliet"),
    ("Juliet", "Tybalt"),
    ("Juliet", "Friar Laurence"),
    ("Juliet", "Romeo"),
    ("Juliet", "Capulet"),
    ("Capulet", "Tybalt"),
    ("Capulet", "Escalus"),
    ("Capulet", "Paris"),
    ("Romeo", "Friar Laurence"),
    ("Romeo", "Benvolio"),
    ("Romeo", "Montague"),
    ("Romeo", "Mercutio"),
    ("Benvolio", "Montague"),
    ("Montague", "Escalus"),
    ("Escalus", "Mercutio"),
    ("Escalus", "Paris"),
    ("Mercutio", "Paris"),
]

ALGORITHMS = ["recommend_by_number_of_common_friends", "recommend_by_influence"]


def algorithm_difference(graph, nodes, results_filename):
    """Identify if the algorithm results are different."""
    same = 0
    different = 0

    with open(results_filename, "w") as file:
        for node in nodes:
            if rcf(graph, node) == rif(graph, node):
                same += 1
                file.write("Same\n")
            else:
                different += 1
                file.write("Different\n")

        file.write("\n")
        file.write(f"Same: {same}\n")
        file.write(f"Different: {different}\n")


def average_ranking(user1, user2, user1_recommendations, user2_recommendations):
    """Return the average ranking of two users from their recommendations."""

    if user1 in user2_recommendations and user2 in user1_recommendations:
        user1_rank = user2_recommendations.index(user1) + 1
        user2_rank = user1_recommendations.index(user2) + 1
        return (user1_rank + user2_rank) / 2

    return None


def get_user_recommendations(graph, user, algorithm):
    """Return user recommendations based on algorithm."""

    if algorithm == ALGORITHMS[0]:
        return rcf(graph, user)

    return rif(graph, user)


def algorithms_average(graph, user1, user2):
    """Return recommendation algorithm average scores."""

    common_average = 0
    influence_average = 0
    for algorithm in ALGORITHMS:
        user1_recommendations = get_user_recommendations(graph, user1, algorithm)
        user2_recommendations = get_user_recommendations(graph, user2, algorithm)

        average = average_ranking(
            user1, user2, user1_recommendations, user2_recommendations
        )
        if average is None:
            return None

        if algorithm == ALGORITHMS[0]:
            common_average = average
        else:
            influence_average = average

    return {ALGORITHMS[0]: common_average, ALGORITHMS[1]: influence_average}


def compare_algorithms(graph, edges):
    """Compare algorithms and return the better one with average performace for each."""

    edge = random.choice(edges)
    user1 = edge[0]
    user2 = edge[1]
    graph.remove_edge(user1, user2)

    average_results = algorithms_average(graph, user1, user2)
    graph.add_edge(user1, user2)

    better_algorithm = None
    if not average_results:
        return better_algorithm

    common_friends_average = average_results["recommend_by_number_of_common_friends"]
    influence_average = average_results["recommend_by_influence"]

    if common_friends_average < influence_average:
        better_algorithm = ALGORITHMS[0]

    if influence_average < common_friends_average:
        better_algorithm = ALGORITHMS[1]

    return {
        "better_algorithm": better_algorithm,
        "common_friends_average": common_friends_average,
        "influence_average": influence_average,
    }


def algorithm_analysis(graph, edges, results_filename):
    """Generate a report on the results of both algorithms."""
    common_friends_algorithm = 0
    influence_algorithm = 0
    neither_algorithm = 0

    with open(results_filename, "w") as file:
        for _ in range(1, 101):
            result = compare_algorithms(graph, edges)
            if result is None:
                neither_algorithm += 1
                continue

            file.write(
                f"Average rank common friends algorithm: {result['common_friends_average']}\n"
            )
            file.write(
                f"Average rank influence algorithm: {result['influence_average']}\n"
            )

            if result["better_algorithm"] == ALGORITHMS[0]:
                common_friends_algorithm += 1
                file.write(f"Number of common friends algorithm is better\n")
            if result["better_algorithm"] == ALGORITHMS[1]:
                influence_algorithm += 1
                file.write(f"Influence algorithm is better\n")
            if result["better_algorithm"] is None:
                neither_algorithm += 1
                file.write(f"None is better\n")
            file.write("\n")

        file.write(f"Number of common friends algorithm: {common_friends_algorithm}\n")
        file.write(f"Influence algorithm: {influence_algorithm}\n")
        file.write(f"Neutral: {neither_algorithm}\n")


if __name__ == "__main__":
    rj_graph = nx.Graph()
    rj_graph.add_nodes_from(CHARACTERS)
    rj_graph.add_edges_from(RELATIONSHIPS)

    algorithm_difference(rj_graph, CHARACTERS, "results/rj_algorithm_diff.txt")
    algorithm_analysis(rj_graph, RELATIONSHIPS, "results/rj_algorithm_analysis.txt")
