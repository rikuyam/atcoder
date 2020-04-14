# ABC014D - 閉路

import sys
input = sys.stdin.buffer.readline

from collections import defaultdict, deque

n=int(input())
tree = defaultdict(set)
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    tree[a].add(b)
    tree[b].add(a)

root=0
parent = [None]*n
parent[root] = -1
depth = [None]*n
depth[root] = 0

stack=deque([root])
while stack:
    node = stack.pop()
    for next in tree[node]:
        if parent[next]==None:
            parent[next]=node
            depth[next]=depth[node]+1
            stack.append(next)

k_max=(n-1).bit_length()
d_table=[[-1]*n for i in range(k_max+1)]
d_table[0]=parent[:]
for k in range(k_max):
    for v in range(n):
        if d_table[k][v]>=0:
            d_table[k+1][v] = d_table[k][d_table[k][v]]

def lcd(node1,node2):
    dd = depth[node2] - depth[node1]

    if depth[node1]>depth[node2]:
        node1,node2=node2,node1
        dd = -dd

    while dd:
        node2 = d_table[dd.bit_length()-1][node2]
        dd-=1<<dd.bit_length()-1

    if node1 == node2:
        return node1;

    for k in range(k_max-1,-1,-1):
        if d_table[k][node1] != d_table[k][node2]:
                node1 = d_table[k][node1];
                node2 = d_table[k][node2];
    return d_table[0][node1]

q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    print(depth[a-1]+depth[b-1]-2*depth[lcd(a-1,b-1)]+1)