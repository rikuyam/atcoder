def main():
    n=int(input())
    d=[[0 for i in range(n+1)]]
    for i in range(1,n+1):
        d.append([0])
        for x in map(int,input().split()):
            d[i].append(x)

    #二次累積和
    for i in range(n+1):
        for j in range(n+1):
            if i==0 and j==0:
                continue
            if i==0:
                d[i][j]+=d[i][j-1]
            elif j==0:
                d[i][j]+=d[i-1][j]
            else:
                d[i][j]+=d[i-1][j]+d[i][j-1]-d[i-1][j-1]

    #O(n**4)
    m=[0 for i in range(n**2+1)]
    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(x1+1,n+1):
                for y2 in range(y1+1,n+1):
                    m[(x2-x1)*(y2-y1)]=max(m[(x2-x1)*(y2-y1)],d[y2][x2]-d[y2][x1]-d[y1][x2]+d[y1][x1])

    for i in range(n**2):
        m[i+1]=max(m[i+1],m[i])

    q=int(input())
    ans=[]
    for i in range(q):
        p=int(input())
        ans.append(m[p])
    for i in ans:
        print(i)

main()