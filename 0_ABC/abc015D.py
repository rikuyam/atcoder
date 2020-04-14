# ABC015D - 高橋くんの苦悩

import numpy as np

w=int(input())
n,k=map(int,input().split())

dp=np.zeros((k+1,w+1),dtype=np.int64)
for i in range(n):
    a,b=map(int,input().split())
    for j in range(k-1,-1,-1):
        dp[j+1,a:]=np.maximum(dp[j+1,a:],dp[j,:-a]+b)
        
print(dp[-1,-1])