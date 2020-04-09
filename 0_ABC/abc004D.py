def main():
    lr,lg,lb=map(int,input().split())
    ans=10**9
    def f(r,l,o):
        if l<r:
            r,l=l,r
        if r>=o:
            return (l-r+1)*(r-o+l-o)//2
        elif l<=o:
            return (l-r+1)*(-r+o-l+o)//2
        else:
            return (l-o+1)*(l-o)//2+(o-r+1)*(-r+o)//2
    for g in range(-500,201):
        ans_g=f(g,g+lg-1,0)
        ans_r=10**9
        for r in range(g-1,-801,-1):
            ans_r=min(ans_r,f(r-lr+1,r,-100))
        ans_b=10**9
        for b in range(g+lg,801):
            ans_b=min(ans_b,f(b,b+lb-1,100))
        ans=min(ans,ans_r+ans_g+ans_b)
    print(ans)

main()