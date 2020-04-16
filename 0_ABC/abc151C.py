# ABC151C - Welcome to AtCoder

n,m=map(int,input().split())
acs=[0]*n
was=[0]*n

for i in range(m):
    p,s=input().split()
    p=int(p)
    if s=="AC":
        acs[p-1]+=1
    else:
        if not acs[p-1]:
            was[p-1]+=1

ac,wa=0,0
for i in range(n):
    if acs[i]:
        ac+=1
        wa+=was[i]

print(ac,wa)