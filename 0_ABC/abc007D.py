def main():
    a,b=map(int,input().split())
    a-=1
    def f(n):
        s=str(n)
        ret=""
        for i in range(len(s)):
            c=int(s[i])
            if c<4:
                ret+=str(c)
            elif c==4:
                ret+='3'+'7'*(len(s)-i-1)
                break
            elif c<9:
                ret+=str(c-1)
            elif c==9:
                ret+='7'*(len(s)-i)
                break
            else:
                print("error")
        return ret
    print(b-a+int(f(a),8)-int(f(b),8))

main()