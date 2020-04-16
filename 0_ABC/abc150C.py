# ABC150C - Count Order

n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))

a,b=0,0

l=[i for i in range(1,n+1)]

for i in range(n-1):
    for j in range(n):
        if l[j]==p[i]:
            l.pop(j)
            break
    tmp=j
    for j in range(1,n-i):
        tmp*=j
    a+=tmp

l=[i for i in range(1,n+1)]

for i in range(n-1):
    for j in range(n):
        if l[j]==q[i]:
            l.pop(j)
            break
    tmp=j
    for j in range(1,n-i):
        tmp*=j
    b+=tmp
        
print(abs(a-b))