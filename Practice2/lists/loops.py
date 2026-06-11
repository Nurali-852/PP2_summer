#1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#3 A short hand for loop that will print all items in a list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#4
#without comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#with
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#5
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#6
newlist = [x.upper() for x in fruits if x == "apple"]
print(newlist)