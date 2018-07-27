# Check if a string can be formed by the concatenation of any strings in a list
s=input()
a=[i for i in input().split()]

#This function will return boolean
def f(s,a):
    if s=='':
        return True

    #loop through the array and find if a there is a string with which the given string starts
    for i in range(len(a)):
        e=a[i]
        if s.startswith(e):
            a.pop(i)
            if f(s[len(e):],a):
                return True
            a.insert(i,e)
    return False

print(f(s,a))
