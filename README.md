# Recommendation System

[![Build Status](https://travis-ci.org/KengoWada/recommendation_system.svg?branch=master)](https://travis-ci.org/KengoWada/recommendation_system) [![Coverage Status](https://coveralls.io/repos/github/KengoWada/recommendation_system/badge.svg?branch=master)](https://coveralls.io/github/KengoWada/recommendation_system?branch=master) [![Maintainability](https://api.codeclimate.com/v1/badges/c786cd4b6b90ee0c88be/maintainability)](https://codeclimate.com/github/KengoWada/recommendation_system/maintainability)

A lot of apps we use today recommend various things to us such as Netflix recommending movies, Facebook recommending friends and many others. In this project I look at potential ways I could do this myself.

This project is inspired by the [University of Washington Computer Science Assignment](https://courses.cs.washington.edu/courses/cse140/13wi/homework/hw4/homework4.html)

## Background

The actual algorithms used by big tech companies are well guarded secrets, but generally there are two approaches: collaborative filtering and content-based filtering.

- **Collaborative Filtering** says that, if your past behavior/preferences were similar to some other user's, then your future behavior may be as well. As a concrete example, suppose that you like John, Paul, and George, and other people like John, Paul, George, and Ringo. Then it stands to reason that you will like Ringo as well, even if you had never previously heard of him. The recommender system does not have to understand anything about what “John”, “Paul”, “George”, and “Ringo” are — they could even be brands of toilet paper, and the algorithm would work identically.

- **Content-based Filtering** considers the characteristics of the things you like, and it recommends similar sorts of things. For instance, if you like “Billie Jean”, “Crazy Train”, and “Don't Stop the Music”, then you might like other songs in the key of F-sharp minor, such as Rachmaninoff's “Piano Concerto No. 1”, even if no one else has ever had that particular set of favorite songs before.

## Graphs

A graph represents relationships among things. The things are represented as **nodes**, and the relationships are represented as **edges**.

One common use for a graph is to represent travel possibilities, such as on a road map or airline map. The nodes of the graph are cities, and the edges show which cities are directly connected. Then, you can use the graph to plan travel.

### Representing Graphs in Python

The [NetworkX](https://networkx.github.io/) library is used to represent graphs in python. Work through the [tutorial](https://networkx.github.io/documentation/stable/tutorial.html) up to and including [Accessing edges and neighbours](https://networkx.github.io/documentation/stable/tutorial.html#accessing-edges-and-neighbors)

**Note:** Look at the **intro** directory for sample **networkx** code

## Recommendation by Number of Common Friends

If someone, that is not your friend, is your friends friend then maybe this person should be your friend too. If this person is friends with more of your friends then they become an even better recommendation. The best friend recommendation is the person with whom you have the largest number of mutual friends.

## Recommendation by Influence

Consider this hypothetical situation:

- Two of your friends are X and Y

- X has only 2 friends (You and one other person)

- Y has 7 billion friends

- Y and X have no other friends on common other than you

Since X is highly selective in terms of friendship, and is a friend of yours, you are likely to have a lot in common with Xs other friends. On the other hand, Yis indiscriminate and there is little reason to believe that you should be friendly with any particular one of Ys other friends.

Incorporate the above idea into your friend recommendation algorithm. Here is the concrete way that you will do so. We call the technique “influence scoring”.
Suppose that user1 and user2 have three friends in common: f1, f2, and f3. The score for user2 as a friend of user1 is 1/numfriends(f1) + 1/numfriends(f2) + 1/numfriends(f3), where numfriends(f) is the number of friends that f has. In other words, each friend F of user1 has a total influence score of 1 to contribute, and divides it equally among all of F's friends.
