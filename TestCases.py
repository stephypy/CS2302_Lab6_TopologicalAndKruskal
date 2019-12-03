# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 6 - Topological and Kruskal
# Instructor: Diego Aguirre
# TA: Gerardo Barraza
# Date of last modification: December 2, 2019
# Purpose: Implement Topological Sort and Kruskals Algorithm

from lab6.topological import Topological
from lab6.graph_al import GraphAL
from lab6.kruskal import Kruskal
from lab6.graph_am import GraphAM


# Assumptions: Topological Sort uses Graph in AL and MUST be directed
def topological_test():
    T = Topological()

    # Test Case 1: Empty Graph AL
    print('[1]Empty Graph\n', 'Before Topological Sort:')
    g = GraphAL(6, directed=True)
    g.display()
    ans = T.topological_sort(g)
    print('\nAfter Topological Sort: \n', ans, '\n---------------------')

    # Test Case 2: Normal Behavior
    print('[2]Normal Behavior\n', 'Before Topological Sort:')
    g.insert_edge(0, 1)
    g.insert_edge(0, 4)
    g.insert_edge(1, 2)
    g.insert_edge(1, 4)
    g.insert_edge(2, 3)
    g.insert_edge(4, 5)
    g.insert_edge(5, 2)
    g.insert_edge(5, 3)
    g.display()
    ans = T.topological_sort(g)
    print('\nAfter Topological Sort: \n', ans, '\n---------------------')

    # Test Case 3: Ascending Linked List look-alike Graph AL (ex: 0 linked to 1, 1 linked to 2 etc no links back to 0)
    print('[3]Ascending and Linked:\n', 'Before Topological Sort:')
    g3 = GraphAL(4, directed=True)
    for i in range(3):
        g3.insert_edge(i, i + 1)
    g3.display()
    ans = T.topological_sort(g3)
    print('\nAfter Topological Sort: \n', ans, '\n---------------------')


# Assumptions: Kruskals uses Graph in AM and MUST be weighted
def kruskal_test():
    K = Kruskal()

    # Test Case 1: Empty Graph AM
    print('[1]Empty Graph\n', 'Before Kruskal:')
    g = GraphAM(5, weighted=True)
    g.display()
    print('\nAfter Kruskal:')
    ans = K.kruskal(g)
    ans.display()
    print('\n---------------------')

    # Test Case 2: Normal Behavior
    print('[2]Normal Behavior\n', 'Before Kruskal:')
    g.insert_edge(0, 1, 10)
    g.insert_edge(0, 3, 8)
    g.insert_edge(1, 2, 9)
    g.insert_edge(1, 3, 1)
    g.insert_edge(1, 4, 5)
    g.insert_edge(2, 4, 2)
    g.insert_edge(3, 4, 4)
    g.display()
    print('\nAfter Kruskal:')
    ans = K.kruskal(g)
    ans.display()
    print('\n---------------------')

    # Test Case 3: Ascending Linked List look-alike Graph AM (ex: 0 linked to 1, 1 linked to 2 etc no links back to 0)
    print('[3]Ascending and Linked:\n', 'Before Kruskal:')
    g3 = GraphAM(4, weighted=True)
    for i in range(3):
        g3.insert_edge(i, i + 1, (i + 1) * 2)
    g3.display()
    print('\nAfter Kruskal:')
    ans = K.kruskal(g3)
    ans.display()


def main():
    print('T O P O L O G I C A L')
    topological_test()
    print('\n K R U S K A L')
    kruskal_test()


main()
