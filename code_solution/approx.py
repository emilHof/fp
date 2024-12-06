"""
Author: Emil Hofstetter
Honor Code: All work herein adheres to the JMU honor code.
"""
from collections import defaultdict, deque
from itertools import permutations, pairwise
from math import inf

"""
Approximate solution taken from Nearest neighbor algorithm.
[Nearest neighbour algorithm](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm)
"""
def solution(edges):
    # first we create the graph
    G = defaultdict(dict)
    V = set()
    for u, v, w in edges:
        V |= {u, v}
        G[u][v] = w
        G[v][u] = w

    # then we find the MST of G
    P = {u: u for u in V}
    R = {u: 1 for u in V}
    def find(a):
        if P[a] != a:
            P[a] = find(P[a])
        return P[a]

    def union(a, b):
        pa = find(a)
        pb = find(b)
        print(a, b, pa, pb)
        if pa == pb:
            return False

        if R[pa] > R[pb]:
            P[pb] = pa
            R[pa] += R[pb]
        else:
            P[pa] = pb
            R[pb] += R[pa]
        return True

    edges.sort(key=lambda x: x[2])
    MST = defaultdict(list)
    for u, v, w in edges:
        if union(u, v):
            MST[u].append(v)
            MST[v].append(u)
    
    # create the preorder traversal of MST
    PO = []
    S = set()
    def po(u):
        nonlocal PO, MST
        S.add(u)
        PO.append(u)
        for v in MST[u]:
            if v in S:
                continue
            po(v)
    po(list(P.keys())[0])
    PO += [PO[0]]

    # now add the path weight between ever neighbor in the PO to the total
    W = 0
    for a, b in pairwise(PO):
        W += G[a][b]
    return [W, PO]




    # now try each ordering of the vertices
    R = [inf, []]
    for order in permutations(V, len(V)):
        print(order)
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
[nv, ne] = [int(a) for a in input().split(" ")]
e = []
for _ in range(ne):
    [a, b, w] = input().split(" ")
    e.append((a, b, int(w)))
"""
e = [
    ("a", "b", 3), 
    ("a", "c", 10),
    ("a", "d", 20),
    ("b", "c", 4), 
    ("b", "d", 5), 
    ("c", "d", 5), 
]
r = solution(e)
print(r[0])
print(" ".join(r[1]))

                

                
