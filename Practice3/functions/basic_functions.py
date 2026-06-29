#1
def my_function():
    print("Hello from a function")

my_function(), my_function()

#2
t1 = 77
c1 = (t1 - 32) * 5 / 9
print(c1)

t2 = 95
c2 = (t2 - 32) * 5 / 9
print(c2)

t3 = 50
c3 = (t3 - 32) * 5 / 9
print(c3)

def f_to_c(t):
    return (t - 32) * 5 / 9

print(f_to_c(77))
print(f_to_c(95))
print(f_to_c(50))

#3
def get_greetings():
    return "Hello"

message = get_greetings()
print(message)
print(get_greetings())

#4
def my_func():
    pass
print(my_func())