"""
Author: Emil Hofstetter
Honor Code: All work herein adheres to the JMU honor code.
"""
from collections import defaultdict 
from itertools import permutations, pairwise
from math import inf
def solution(edges):
    G = defaultdict(dict)
    V = set()
    for u, v, w in edges:
        V |= {u, v}
        G[u][v] = w
        G[v][u] = w

    # now try each ordering of the vertices
    R = [inf, []]
    for order in permutations(V, len(V)):
        order = list(order) + [list(order)[0]]
        # now see if we can walk like this
        r = 0
        for u, v in pairwise(order):
            if v not in G[u]:
                r = inf
                break
            r += G[u][v]
        if R[0] > r:
            R = [r, order]
    return R



"""
e = [
    ("a", "b", 5), 
    ("a", "c", 3),
    ("a", "d", 2),
    ("b", "c", 5), 
    ("b", "d", 10), 
    ("c", "d", 1), 
]
[nv, ne] = [int(a) for a in input().split(" ")]
e = []
for _ in range(ne):
    [a, b, w] = input().split(" ")
    e.append((a, b, int(w)))
r = solution(e)
print(r[0])
print(" ".join(r[1]))
"""

                

