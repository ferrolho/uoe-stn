#!/usr/bin/python3

import math
import networkx as nx
import sys
import time

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def entropy1(g):
    if nx.number_of_nodes(g) == 0:
        return 0
    diff_degrees = sum(x > 0 for x in nx.degree_histogram(g)) - 1
    return diff_degrees / nx.number_of_nodes(g)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def averageDegree(g):
    return sum(g.degree(node) for node in g.nodes()) / nx.number_of_nodes(g)

def entropy2(g):
    avg_deg = averageDegree(g)
    return math.sqrt(sum((g.degree(node) - avg_deg) ** 2 for node in g.nodes())) / nx.number_of_nodes(g)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

g = nx.Graph()

print('Loading graph from file...')

for i, line in enumerate(sys.stdin):
	print('Reading line no. {}'.format(i), end='\r')

	if line[0] == '#':
		continue

	src, dst = line.split('\t')
	g.add_edge(src, dst)

print('Graph successfully loaded')
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

start_time = time.time()
entropy = entropy1(g)
elapsed_time = time.time() - start_time

print('Entropy 1:', entropy)
print('{:.4f}s'.format(elapsed_time))
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

start_time = time.time()
entropy = entropy2(g)
elapsed_time = time.time() - start_time

print('Entropy 2:', entropy)
print('{:.4f}s'.format(elapsed_time))
print()
