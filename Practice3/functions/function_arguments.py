#!
def my_func(fname):
    return fname + "Refsnes"

print(my_func("Emil"))
print(my_func("Kairat Nurtas"))
print(my_func("Linus"))

#2
def message(name): # name we call parameter
    return "Hello " + name

print(message("Nurali")) # Nurali we call argument

#3 Number of arguments
def func(rname, lname):
    return rname + " " + lname

print(func("Danil", "Kolbasenko"))

#4
"""
ERROR cause it should call exactly 2 arguments as defined

def func(rname, lname):
    print rname + " " + lname

print(func("Danil"))
"""

#5
def func(name = "friend"):
    return "Hello dear " + name

print(func("Niko"))
print(func())

#6
def func(animal, name):
    print("I have a", animal)
    print("My" + animal + "'s name is" + name)

func(name = "strom", animal = "dog") #if use key = value order does not matter
#Keyword Arguments = kwargs

#7
func("dog", "storm") # positional agruments

#8
#Positional must come before kwargs
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#9
# any data type can be argument for a function
def func(fruits):
    for fruit in fruits:
        print(fruit.upper())

my_list = ["banana", "apple", "mellon"]
func(my_list)

#10
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#11 Positiional only args
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

#12 Keyword-only args
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

#13 combining
def func(a, b, /, *, c, d):
   return a + b + c + d

ans = func(5, 10, d = 15, c = 20)
print(ans)