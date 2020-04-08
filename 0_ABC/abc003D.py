MOD=10**9+7

def combination_mod(n,k,mod=MOD):
    def comb(n,k,MOD):
        if n<0 or k<0 or n<k:
            return 0
        return table[n]*(table_inv[k]*table_inv[n-k]%mod)%mod

    mod = MOD
    table = [1,1] #元テーブル
    table_inv = [1,1] #逆元テーブル
    inverse = [0,1] #逆元テーブル計算用テーブル

    for i in range(2,n+1):
        table.append((table[-1]*i)%mod)
        inverse.append((-inverse[mod%i]*(mod//i))%mod)
        table_inv.append((table_inv[-1]*inverse[-1])%mod)

    return comb(n,k,mod)

def main():
    r,c=map(int,input().split())
    x,y=map(int,input().split())
    d,l=map(int,input().split())
    
    ans=(r-x+1)*(c-y+1)
    a=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            a[i][j]=combination_mod(max(x-i,0)*max(y-j,0),d+l)
    a[2][1]-=a[2][2]
    a[1][2]-=a[2][2]
    a[2][0]-=2*a[2][1]+a[2][2]
    a[1][1]-=a[2][1]+a[1][2]+a[2][2]
    a[0][2]-=2*a[1][2]+a[2][2]
    a[1][0]-=a[2][0]+2*a[1][1]+2*a[2][1]+a[1][2]+a[2][2]
    a[0][1]-=2*a[1][1]+a[0][2]+a[2][1]+2*a[1][2]+a[2][2]
    a[0][0]-=2*a[1][0]+2*a[0][1]+a[2][0]+4*a[1][1]+a[0][2]+2*a[2][1]+2*a[1][2]+a[2][2]
    ans*=a[0][0]%MOD

    ans*=combination_mod(d+l,d)
    ans%=MOD
    print(ans)

main()