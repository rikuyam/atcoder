# ABC017C - ハイスコア

n,m=map(int,input().split())
lrs=[list(map(int,input().split()))for i in range(n)]

arr=[0]*(m+1)
ans=0
for l,r,s in lrs:
    arr[l-1]+=s
    arr[r]-=s
    ans+=s

for i in range(m):
    arr[i+1]+=arr[i]

print(ans-min(arr[:-1]))