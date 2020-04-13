# ABC162C - Sum of gcd of Tuples (Easy)

import sys
input = sys.stdin.buffer.readline

import math as m

def main():
    n=int(input())
    d=[[[None]*n for i in range(n)]for j in range(n)]
    ans=0

    for i in range(n):
        for j in range(i,n):
            ij=m.gcd(i+1,j+1)
            for k in range(j,n):
                d[i][j][k]=m.gcd(ij,k+1)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i<=j and j<=k:
                    ans+=d[i][j][k]
                elif i<=k and k<=j:
                    ans+=d[i][k][j]
                elif j<=i and i<=k:
                    ans+=d[j][i][k]
                elif j<=k and k<=i:
                    ans+=d[j][k][i]
                elif k<=i and i<=j:
                    ans+=d[k][i][j]
                elif k<=j and j<=i:
                    ans+=d[k][j][i]
    print(ans)

main()
