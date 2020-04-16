# ABC018D - バレンタインデー

import itertools

n_max,m_max,p,q,r=map(int,input().split())

yz=[[] for i in range(n_max)]
for _ in range(r):
    x,y,z = map(int,input().split())
    yz[x-1].append(tuple([y-1,z]))

ans=0
for ns in itertools.combinations(range(n_max),p):
    ms=[0]*m_max
    for n in ns:
        for y,z in yz[n]:
            ms[y]+=z
    ms.sort(reverse=1)
    ans=max(ans,sum(ms[:q]))

print(ans)
