from collections import *
def merge(a,l,m,r):
    t1,t2=deque(),deque()
    for e in a[l:m+1]:
        t1.append(e)
    for e in a[m+1:r+1]:
        t2.append(e)
    for i in range(l,r+1):
        if t1[0]<t2[0]:
            a[i]=t1.popleft()
        elif t2[0]<=t1[0]:
            a[i]=t2.popleft()
        if t1==deque():
            a[i+1:r+1]=list(t2)
            break
        elif t2==deque():
            a[i+1:r+1]=list(t1)
            break
    # return a

def mergesort(a,l,r):
    if l<r:
        m=(l+r)//2
        mergesort(a,l,m)
        mergesort(a,m+1,r)
        merge(a,l,m,r)

n=int(input())
a=[int(i) for i in input().split()]
mergesort(a,0,n-1)
print(a)
