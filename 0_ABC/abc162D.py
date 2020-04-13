# ABC162D - RGB Triplets

import numpy as np
from numba import njit

def main():
    n=int(input())
    s=np.zeros(n,dtype=np.int64)
    a=input()
    for i in range(n):
        s[i]=ord(a[i])%3
    ans=0
    d=np.zeros((3,n),dtype=np.int64)
    m=np.zeros((3,n),dtype=np.int64)
    l=np.array([[0,2,1],[2,1,0],[1,0,2]])
    #print(s.dtype,d.dtype,m.dtype)

    for i in range(n):
        d[s[i],i]=1
        m[s[i],i]=1

    for j in range(3):
        for i in range(n-1,0,-1):
            m[j,i-1]+=m[j,i]

    print(f(n,s,m,d,l))

@njit
def f(n,s,m,d,l):
    ans=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            if s[i]==s[j]:
                continue
            ans+=m[l[s[i]][s[j]],j+1]
            if (j*2-i)<n:
                ans-=d[l[s[i]][s[j]],j*2-i]
    return ans
        
main()
