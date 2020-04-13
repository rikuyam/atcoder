# ABC162B - FizzBuzz Sum

import sys
input = sys.stdin.buffer.readline

def main():
    n=int(input())
    ans=0
    for i in range(n+1):
        if i%3==0:
            continue
        if i%5==0:
            continue
        ans+=i
    print(ans)

main()