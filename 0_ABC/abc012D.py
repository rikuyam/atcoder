#ABC012D - バスと避けられない運命

import sys
from collections import defaultdict
input = sys.stdin.buffer.readline

from scipy.sparse.csgraph import floyd_warshall

def main():
    inf = 10**9

    n,m = map(int,input().split())
    costs = [[inf]*n for i in range(n)] 
    for i in range(m):
        a,b,t = map(int,input().split())
        costs[a-1][b-1] = t
        costs[b-1][a-1] = t
    for i in range(n):
        costs[i][i] = 0

    ans=inf
    for tmp in floyd_warshall(costs):
        ans=min(ans,max(tmp))
    print(int(ans))

main()