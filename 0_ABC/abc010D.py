#ABC010D - 浮気予防

import sys
from collections import defaultdict
input = sys.stdin.buffer.readline

# Dinic's algorithm O(node**2 * edge)
from collections import deque
class Dinic:
    def __init__(self, n, inf = 1000000007):# n: ノード数
        self.n = n
        self.inf = inf
        self.G = [[] for _ in range(n)]
        self.level = [0 for _ in range(n)]
        self.iter = [0 for _ in range(n)]

    def add_edge(self, fr, to, cap):# fr:from node, to:to node, cap:edge capacity
        # to: 行き先, cap: 容量, rev: 反対側の辺
        self.G[fr].append({'to':to, 'cap':cap, 'rev':len(self.G[to])})
        self.G[to].append({'to':fr, 'cap':0, 'rev':len(self.G[fr])-1})

    def add_multi_edge(self, a, b, cap):# a:node1, b:node2, cap:edge capacity
        # to: 行き先, cap: 容量, rev: 反対側の辺
        self.G[a].append({'to':b, 'cap':cap, 'rev':len(self.G[b])})
        self.G[b].append({'to':a, 'cap':cap, 'rev':len(self.G[a])-1})

    # sからの最短距離をbfsで計算
    def bfs(self, s):
        self.level = [-1 for _ in range(self.n)]
        self.level[s] = 0;
        queue = deque()
        queue.append(s)
        while queue:
            v = queue.popleft()
            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if e['cap'] > 0 and self.level[e['to']] < 0:
                    self.level[e['to']] = self.level[v] + 1
                    queue.append(e['to'])

    # 増加バスをdfsで探す
    def dfs(self, v, t, f):
        if v == t: return f
        for i in range(self.iter[v], len(self.G[v])):
            self.iter[v] = i
            e = self.G[v][i]
            if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
                d = self.dfs(e['to'], t, min(f, e['cap']))
                if d > 0:
                    e['cap'] -= d
                    self.G[e['to']][e['rev']]['cap'] += d
                    return d

        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            # bfsで到達不可
            if self.level[t] < 0 : return flow
            self.iter = [0 for _ in range(self.n)]
            f = self.dfs(s, t, self.inf)
            while f > 0:
                flow += f
                f = self.dfs(s,t, self.inf)


def main():
    n,g,e=map(int,input().split())
    p=list(map(int,input().split()))

    di = Dinic(n+1)

    for _ in range(e):
        a,b=map(int,input().split())
        di.add_multi_edge(a,b,1)
    
    for i in p:
        di.add_multi_edge(i,n,1)

    print(di.max_flow(0,n))

        

    



main()