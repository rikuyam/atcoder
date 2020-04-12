#ABC011D - 大ジャンプ

import sys
input = sys.stdin.buffer.readline

def main():
    n,d=map(int,input().split())
    x,y=map(abs,map(int,input().split()))
    
    if x%d or y%d:
        print(0)
        sys.exit()
    
    x//=d
    y//=d

    if (n-x-y)%2:
        print(0)
        sys.exit()

    pascal=[[0]*(i+1) for i in range(n+1)]
    pascal[0][0]=1
    for i in range(n):
        for j in range(i+1):
            pascal[i+1][j]+=pascal[i][j]
            pascal[i+1][j+1]+=pascal[i][j]

    ans=0
    for i in range((n-x-y)//2+1):
        j=(n-x-y)//2-i
        tmp=1
        tmp*=pascal[n][x+i]
        tmp*=pascal[n-(x+i)][y+j]
        tmp*=pascal[n-(x+i)-(y+j)][i]
        ans+=tmp
    print(ans/(4**n))

main()