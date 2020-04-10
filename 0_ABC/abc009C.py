#ABC009C - 辞書式順序ふたたび

def f(k,c,s1,m1):
        s=s1[:]
        m=m1[:]
        m.remove(c)
        for i in m:
            if i in s:
                s.remove(i)
            else:
                k-=1
        return k>=0

def main():
    n,k=map(int,input().split())
    s=list(input())
    m=sorted(s)
    ans=""
    for i in range(n):
        for c in m:
            if f(k-1+(c==s[i]),c,s[i+1:],m):
                ans+=c
                m.remove(c)
                if c != s[i]:
                    k-=1
                break
    print(ans)

main()