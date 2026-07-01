#Enumerate
x = ('apple', 'banana', 'cherry')  

y = enumerate(x)      # parameter start = 0(default)

print(list(y))   # [(0, 'apple'), (1, 'banana'), (2, 'cherry')] 


#ZIP   zip(a,b,c ...)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")   

x = zip(a, b)     # pairs elements with corresponding index. IF tuple has more value, it is ignored

print(tuple(x))   #(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))


#ZIP and Enumerate combination
a = [10, 20, 30]
b = ['a', 'b', 'c']

for idx, (num, char) in enumerate(zip(a,b), start=1):  
    print(idx, num, char)                #idx is just index that is defined to  start from 1. other variables names is print them respectively
"""
1 10 a
2 20 b
3 30 c
"""

a = [10, 20, 30]
b = ['a', 'b', 'c']

for idx, (num, char) in enumerate(zip(a,b), start=1):
    print(idx, num, char)
"""
0 sravan java 78
1 bobby python 100
2 ojaswi R 97
3 rohith cpp 89
4 gnanesh bigdata 80
"""

a = ['sravan', 'bobby', 'ojaswi', 'rohith', 'gnanesh']
b = ['java', 'python', 'R', 'cpp', 'bigdata']
c = [78, 100, 97, 89, 80]

for i, t in enumerate(zip(a,b,c)):
    print(i, t)
"""
0 ('sravan', 'java', 78)
1 ('bobby', 'python', 100)
2 ('ojaswi', 'R', 97)
3 ('rohith', 'cpp', 89)
4 ('gnanesh', 'bigdata', 80)
"""
a = ['sravan', 'bobby', 'ojaswi', 'rohith', 'gnanesh']
b = ['java', 'python', 'R', 'cpp', 'bigdata']
c = [78, 100, 97, 89, 80]

for i, t in enumerate(zip(a,b,c)):
    print(i, t[0], t[1])   # if 3 indexes then marks output
"""
0 sravan java 
1 bobby python 
2 ojaswi R 
3 rohith cpp 
4 gnanesh bigdata 
"""