# Python also has a super() function that will make the child class inherit all the methods and properties from its parent
class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#add a parameter year
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Ross", 2000)

#add method
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)