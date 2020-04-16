# ABC018C - 菱型カウント
# only PyPy

r,c,k=map(int,input().split())
m=[[0]*(c+2)] + [[0]+[int(s=="o") for s in input()]+[0] for i in range(r)] + [[0]*(c+2)]

#print(m)
a=[[0]*(c+2) for _ in range(r+2)]
b=[[0]*(c+2) for _ in range(r+2)]

for i in range(1,r+1):
    for j in range(1,c+1):
        if m[i][j]!=0:
            a[i][j]+=a[i-1][j]+1

for i in range(r,0,-1):
    for j in range(1,c+1):
        if m[i][j]!=0:
            b[i][j]+=b[i+1][j]+1

#print(a[1:-1])
#print(b[1:-1])

for i in range(1,r+1):
    for j in range(1,c+1):
        a[i][j]=min(a[i][j],b[i][j])

#for i in a[1:-1]:
#    print(i[1:-1])
#print()

ans=0
for i in range(1+k-1,r+1+1-k):
    for j in range(1+k-1,c+1+1-k):
        tmp=1
        for d in range(k):
            if a[i][j-d]<k-d or a[i][j+d]<k-d:
                tmp=0
                break
        if tmp:
            ans+=1

print(ans)
