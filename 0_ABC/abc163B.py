# ABC163B - Homework

n,m=map(int,input().split())
a=list(map(int,input().split()))

if n-sum(a)>=0:
    print(n-sum(a))
else:
    print(-1)