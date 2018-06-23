for i in range(n):
    j=i
    t=a[i]
    
    #find the correct position of the current element t 
    while j>0 and t<a[j-1]:
        #shift the elements to the right
        a[j]=a[j-1]
        j-=1
    
    #put the element t to the currect position
    a[j]=t
print(a)
