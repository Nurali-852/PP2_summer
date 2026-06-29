#SCOPE
#1
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#2
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

#3 nonlocal used inside nested loops
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

#4 LEGB
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

#DECORATORS
#1
def changecase(func): #тоесть это основная функция
  def myinner():
    return func().upper()
  return myinner

@changecase #декоратор вызывает базовую функцию как инпут для нижней функции
def myfunction():
  return "Hello Sally"

print(myfunction())

#2
@changecase
def otherfunction():
  return "I am speed!"

print(otherfunction())

#3
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#4
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#5
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

#6
def myfunction(p):
  return "Have a great day!" + p

print(myfunction.__name__)

#7
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

#8
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

#9
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)