#1

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])

#2

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[-4:-1])

#3

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#4
#Change the second item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the second value by replacing it with two new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#5

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#6

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#7
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#8
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#9
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#10
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#11
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
del thislist #delete the list completely

#12
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)