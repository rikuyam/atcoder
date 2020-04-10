#ABC008D - 金塊ゲーム

import sys

sys.setrecursionlimit(10**9)

def calc(x1,y1,x2,y2):
    if (x1,y1,x2,y2) in memo:
        return memo[(x1,y1,x2,y2)]
    ret=0
    for x,y in m:
        if x1<x and x<x2 and y1<y and y<y2:
            tmp=x2-x1+y2-y1-3
            tmp+=calc(x1,y1,x,y)
            tmp+=calc(x,y1,x2,y)
            tmp+=calc(x1,y,x,y2)
            tmp+=calc(x,y,x2,y2)
            ret=max(ret,tmp)
    memo[(x1,y1,x2,y2)]=ret
    return ret

def main():
    global m
    w,h=map(int,input().split())
    n=int(input())
    m=tuple(tuple(map(int,input().split()))for _ in range(n))
    print(calc(0,0,w+1,h+1))

memo=dict()
m=[]
main()