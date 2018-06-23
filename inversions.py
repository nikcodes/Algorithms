from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    a=[int(input()) for _ in range(n)]
    d=defaultdict(lambda:0)
    b=a.copy()

    def msort(i,j):
        global a
        if i==j:
            return
        m=(i+j)//2
        msort(i,m)
        msort(m+1,j)

        x,y=m,j
        t=[]
        while 1:
            if a[x]>a[y]:
                t.append(a[x])
                d[a[x]]+=y-m
                x-=1
                if x==i-1:
                    t.extend(a[y:m:-1])
                    break

            elif a[x]<a[y]:
                t.append(a[y])
                y-=1
                if y==m:
                    if i:
                        t.extend(a[x:i-1:-1])
                    else:
                        t.extend(a[x::-1])
                    break
        a[i:j+1]=t[::-1]
    msort(0,n-1)
    for e in b:
        print(d[e],end=' ')
    print()
