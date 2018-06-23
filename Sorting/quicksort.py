def pivot(l,r):

    i=l+1
    for j in range(l+1,r+1):

        #comparing with the pivot which is the first element
        if a[j]<=a[l]:
            a[j],a[i]=a[i],a[j]
            i+=1

    #set the pivot to the correct position
    #at position i-1 there is last element which is smaller than the pivot so swap it with pivot
    a[i-1],a[l]=a[l],a[i-1]

    #return the new position of pivot
    return i-1

def quicksort(l,r):
    if l==r or l<0 or r<0 or l>=n or r>=n or l>r :
        return
    p=pivot(l,r)
    quicksort(l,p-1)
    quicksort(p+1,r)


a=[int(i) for i in input().split()]
n=len(a)
quicksort(0,n-1)
print(a)
