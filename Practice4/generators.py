#1

def fun(N):
    cnt = 1
    while cnt <= N:
        yield cnt * cnt
        cnt += 1

N = 4
ans = fun(N)
for i in ans:
    print(i)

#2
def fun2(n):
    for cnt in range(0, n + 1):
        if cnt % 2 == 0:
            yield cnt

a = int(input())
ans = fun2(a)
for i in ans:
    print(str(i) + ", ", end = "")
print(end='\n')

#3
def fun3(n):
    for cnt in range(1, n + 1):
        if cnt % 3 == 0 and cnt % 4 == 0:
            yield cnt

b = int(input())
ans = fun3(b)
for i in ans:
    print(str(i) + ", ", end = "")
print(end='\n')

#4
def square(n):
    for cnt in range(1, n + 1):
        yield cnt * cnt

c = int(input())
for i in square(c):
    print(str(i) + ", ", end="")
print(end='\n')

#5
def back(n):
    for cnt in range(n, 0, -1):
        yield cnt

d = int(input())
for i in back(d):
    print(str(i) + ", ", end = "")