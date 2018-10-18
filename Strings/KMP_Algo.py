t,p=input().split()
n=len(a)
m=len(b)

#constructing the lps array which is of the size of pattern
lps=[0]*m
i=1
l=0 #l is the lps value of the previous index

while i<m:
    if p[i]==p[l]:
        l+=1
        lps[i]=l

    else:
        #if the lps value for the previous position is also 0 then for the current position it will also be 0 so just increment i
        if l==0:
            i+=1
        else:
            #we will find another index which can be matched with ith index. we just update l
            l=lps[l-1]

#the KMP algo
count=0
i=j=0 # i is for text and j for pattern

while i<n:
    #if both the corrosponding characters match then just icrement both the indices
    if t[i]==p[j]:
        i+=1
        j+=1

    #if whole pattern is traversed then increment the count
    if j==m:
        count+=1
        print('pattern found at ending index ',i-1)

        #reinitilise j. if first 4 characters has match the last 4 characters(which is lps[j-1]) then initialise j to 5th character which is also lps[j-1]
        j=lps[j-1]

    elif i<n and t[i]!=p[j]:
        #if it is the first character of the pattern then just increase the index in text
        if j==0:
            i+=1

        else:
            #adjust j according to the previous rule
            j=lps[j-1]
