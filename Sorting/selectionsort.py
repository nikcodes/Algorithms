for i in range(n):
    m=i
    t=a[i]
    for j in range(i+1,n):
        if a[j]<t:
            m=j
            t=a[j]

    a[i],a[m]=a[m],a[i]
print(a)
