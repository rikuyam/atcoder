# ABC148D - Brick Break

import bisect

n=int(input())
a=list(map(int,input().split()))

ans=0
for i in a:
    if ans+1==i:
        ans=i

#print(ans)
if ans:
    print(n-ans)
else:
    print(-1)