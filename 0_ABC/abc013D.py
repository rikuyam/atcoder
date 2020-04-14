# ABC013D - 阿弥陀

import numpy as np

n,m,d=map(int,input().split())
a=np.array(list(map(int,input().split())),dtype=np.int64)

m=np.arange(n+1,dtype=np.int64)

for i in a:
    m[i:i+2]=m[i+1:i-1:-1]
    
table=np.empty(n,dtype=np.int64)
for i in range(n):
    table[m[i+1]-1]=i

ans=np.arange(n,dtype=np.int64)

def prod(a,b):
    global n
    for i in range(n):
        a[i]=b[a[i]]

def pow_(a):
    global n
    ret = np.empty(n,dtype=np.int64)
    for i in range(n):
        ret[i]=a[a[i]]
    return ret

while d:
    if d%2:
        prod(ans,table)
    table = pow_(table)
    #print(table)
    d//=2

for i in ans:
    print(i+1)
