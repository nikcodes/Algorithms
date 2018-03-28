n=int(input())
a=[int(i) for i in input().split()]
d={}
for i in range(1,n):
    j=i;t=a[i]
    while j>0 and t<a[j-1]:
        a[j]=a[j-1]
    a[j]=t
for i in range(n):
    d[a[i]] = i+1
for e in a:
    print(d[e],end=' '
