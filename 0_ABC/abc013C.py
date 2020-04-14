# ABC013C - 節制

n,h=map(int,input().split())
a,b,c,d,e=map(int,input().split())

h-=e*n+1
b+=e
d+=e

ans=a*n

for i in range(n+1):
    if (h+b*i)>=0:
        ans=min(ans,a*i)
        break
    else:
        ans=min(ans,(-(h+b*i)//d+(-(h+b*i)%d>0))*c+a*i)

print(ans)