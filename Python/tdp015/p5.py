# TDP015 Programming Assignment 5
# Graphs
# Skeleton Code

import sys
import json

# In one of my current research projects, I am developing algorithms
# for the parsing of natural language to meaning representations in
# the form of directed graphs:
#
# http://www.ida.liu.se/~marku61/ceniit.shtml
#
# A desirable property of these graphs is that they should be acyclic,
# that is, should not contain any (directed) cycles. Your task in this
# assignment is to implement a Python function that tests this
# property, and to apply your function to compute the number of cyclic
# graphs in one of the datasets that I am using in my research.
#
# Your final script should be callable from the command line as follows:
#
# $ python3 p5.py ccg.train.json
#
# This should print out the IDs of the cyclic graphs in the file:
#
# $ python3 p5.py ccg.train.json
# 22172056
# 22153010
# 22106047
#
# The graphs are stored in a JSON file containing a single dictionary
# mapping graph ids (8-digit integers) to graphs, where each graph is
# represented as a dictionary mapping vertices (or rather their ids)
# to lists of neighbouring vertices.

def cyclic(graph):
    """Test whether the directed graph `graph` has a (directed) cycle.

    The input graph needs to be represented as a dictionary mapping vertex
    ids to iterables of ids of neighboring vertices. Example:

    {"1": ["2"], "2": ["3"], "3": ["1"]}

    Args:
        graph: A directed graph.

    Returns:
        `True` iff the directed graph `graph` has a (directed) cycle.
    """
    def checkForCycles(currentNode, graph, visited):
        visited.append(currentNode)
        nextNodes = graph[currentNode]
        for node in nextNodes:
            if node in visited:
                return True
            if checkForCycles(node, graph, visited): #Deepth First Search
                return True
        # If we reach this point then the branch did not have a cycle and edges leading here 
        # should not be marked as cyclic. Therefor we remove the the node from visited when
        # backtracking.
        # Possibly we should have a "safe" list so that we dont have to dive down here again....
        visited.remove(currentNode)
        return False

    visited = []
    # Brute force checking all nodes in the graph...
    for node in graph:
        if checkForCycles(node, graph, visited):
            return True
    return False

if __name__ == "__main__":
    # Open the file
    with open(sys.argv[1], 'r') as graphFile:
        graphs = json.load(graphFile)

    # Iterate over the graphs
    total = 0
    cg = 0
    for id, graph in graphs.items():
        total += 1
        if cyclic(graph):
            cg += 1
            print("{}".format(id))      
    print("{} cyclic graphs of a total of {}.".format(cg, total))
  
