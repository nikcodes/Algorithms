counting sort
a=[int(i) for i in input().split()]
from collections import defaultdict
d=defaultdict(lambda:0)

#store the frequencies of all elements
for e in a:
    d[e]+=1

#traverse all the numbers from least number till the largest number and append them in a new sorted array according
#to their count

sorteda=[]
for i in range(min(a),max(a)+1):
    sorteda.extend([i]*d[i])

print(sorteda)
