#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#4
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#5
set1 = {"abc", 34, True, 40, "male"}

#6
myset = {"apple", "banana", "cherry"}
print(type(myset))

#7
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#8
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#9
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#10
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#11
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#12
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#13
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#14
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) #If the item to remove does not exist, discard() will NOT raise an error.

#15
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset) #remove random

#16
thisset = {"apple", "banana", "cherry"}

thisset.clear() #empty set

print(thisset)

del thisset # delete set completely