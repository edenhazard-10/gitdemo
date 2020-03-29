#Q3DP
n=eval(input())
a=list(map(int,input().split()))
m=eval(input())
b=list(map(int,input().split()))
A=[0]*(n+1)
def f(q,w):
    if A[w]!=0:
        return A[w]
    Max=A[0]
    for i in range(1,b[t]+1):
        for j in range(1,i+1):
            Max=max(Max,q[j-1]+A[i-j])
            A[i]=Max
    return A[w]