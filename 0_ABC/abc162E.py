# ABC162E - Sum of gcd of Tuples (Hard)

MOD = 10**9+7

n,k=map(int,input().split())
ans=0

gcd=[0]*(k+1)
for i in range(1,k+1):
    gcd[i]=pow(k//i,n,MOD)
for i in range(k//2,0,-1):
    for j in range(i*2,k+1,i):
        gcd[i]-=gcd[j]
for i in range(1,k+1):
    ans+=i*gcd[i]%MOD

print(ans%MOD)