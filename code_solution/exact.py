from collections import defaultdict 
from itertools import combinations
def solution(edges):
    G = defaultdict(set)
    for u, v in edges:
        G[u].add(v)
        G[u].add(u)
        G[v].add(u)
        G[v].add(v)

    # now try each combination
    for i in reversed(range(len(G))):
        for comb in combinations(G.keys(), i):
            S = set(comb)
            valid = True
            for u in comb:
                if len(S - set(G[u])) != 0:
                    valid = False
                    break
            if valid:
                return S
    return []

l = int(input())
e = []
for _ in range(l):
    [a, b] = input().split(" ")
    e.append((a, b))

print(solution(e))

                

