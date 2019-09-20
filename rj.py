from recommendation.main import recommend_by_number_of_common_friends as rcf
from recommendation.main import recommend_by_influence as rif
import networkx as nx

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
