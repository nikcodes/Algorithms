#with each iteration the larger elements are pushed to the back one by one

a=[int(i) for i in input().split())]
n=len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j]>=a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
