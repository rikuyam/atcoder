# ABC009D - 漸化式

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

def matrix_andxor(matrix1,matrix2):
    c1,r1=matrix1.shape
    c2,r2=matrix2.shape
    return np.bitwise_xor.reduce(matrix1[:,:,None]&matrix2[None,:,:],axis=1)

def main():
    k,m=map(int,readline().split())
    a=np.array(readline().split(),np.uint32)
    c0=np.array(readline().split(),np.uint32)

    if m<=k:
        print(a[m-1])
        sys.exit()

    m-=k
    a=a[::-1].reshape(-1,1)
    ie=(1<<32)-1
    c=np.eye(k,k,-1,np.uint32)*ie
    c[0]=c0
    
    while m>0:
        if m&1:
            a=matrix_andxor(c,a)
        c=matrix_andxor(c,c)
        m//=2
    
    print(a[0][0])

main()