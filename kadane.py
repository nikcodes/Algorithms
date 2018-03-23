a=[int(i) for i in input().split()]
m=0
t=0
for e in a:
    t+=e
    if t<=0:
        t=0
    m=max(t,m)
print(m)
