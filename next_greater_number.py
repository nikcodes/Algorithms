for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[]
    for i in range(n-1,-1,-1):
        t=10
        for e in b:
            if e>a[i] and e<t:
                t=e
        if t>a[i] and t!=10:
            dt=a[i]
            a[i]=t
            b.remove(t)
            b.append(dt)
            b.sort()
            a[i+1:]=b
            break
        b.append(a[i])
    for e in a:
        print(e,end='')
    print()
