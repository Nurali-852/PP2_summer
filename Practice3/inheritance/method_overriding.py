class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

#The child's __init__() function overrides the inheritance of the parent's __init__() function.

#To keep inheritance add a call to a parent
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)