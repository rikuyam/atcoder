# ABC147C - HonestOrUnkind2

from collections import defaultdict
import itertools

n = int(input())
m = [[]for i in range(n)]

for i in range(n):
    j = int(input())
    for _ in range(j):
        x,y=map(int,input().split())
        m[i].append([x-1,y])

#print(m)
ans=0
for i in itertools.product([0,1],repeat=n):
    k=1
    for j in itertools.compress([ii for ii in range(n)],i):
        for x,y in m[j]:
            if i[x] !=-1 and i[x]!=y:
                k=0
                break
        if not k:
            break
    #print(i)
    if k:
        ans=max(ans,sum(i))

print(ans)

