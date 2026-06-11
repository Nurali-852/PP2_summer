#1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #key names

#2
for x in thisdict:
  print(thisdict[x]) #values

#3
for x in thisdict.values():
  print(x)

#4
for x in thisdict.keys():
  print(x)

#5
for x, y in thisdict.items():
  print(x, y)

#6
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
mydict2 = dict(thisdict)
print(mydict, "\n", mydict2)

#7
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#8
print(myfamily["child2"]["name"])

#9
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#10
