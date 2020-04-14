# ABC016D - 一刀両断

ax,ay,bx,by=map(int,input().split())
n=int(input())
x=[list(map(int,input().split())) for _ in range(n)]

ans=0
def f(p,q,r,s,x,y):
    return (q-s)*x-(p-r)*y+p*s-q*r

for i in range(n):
    if f(ax,ay,bx,by,x[i-1][0],x[i-1][1])*f(ax,ay,bx,by,x[i][0],x[i][1])<0 and f(x[i-1][0],x[i-1][1],x[i][0],x[i][1],ax,ay)*f(x[i-1][0],x[i-1][1],x[i][0],x[i][1],bx,by)<0:
        ans+=1
print(ans//2+1)