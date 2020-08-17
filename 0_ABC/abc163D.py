# ABC163D - Sum of Large Numbers

MOD=10**9+7
n,k=map(int,input().split())

ans=0
for i in range(k,n+2):
    ans+=(n+(n-i+1)-(i-1+0))*i//2+1
    ans%=MOD
    #print((n+(n-i+1))*i//2,(i-1+0)*i//2,(n+(n-i+1)-(i-1+0))*i//2,ans)

print(ans)