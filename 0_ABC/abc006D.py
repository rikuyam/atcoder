import bisect

def main():
    n=int(input())
    c=[int(input())for i in range(n)]
    dp=[30001 for i in range(n)]

    dp[0]=c[0]
    for i in c[1:]:
        dp[bisect.bisect_left(dp,i)]=i
    print(n-bisect.bisect_left(dp,30001))

main()