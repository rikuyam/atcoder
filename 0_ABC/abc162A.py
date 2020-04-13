# ABC162A - Lucky 7

import sys
input = sys.stdin.buffer.readline

def main():
    s=int(input())
    ans=0
    if s%10==7:
        ans=1
    if (s//10)%10==7:
        ans=1
    if s//100==7:
        ans=1
    if ans:
        print("Yes")
    else:
        print("No")

main()