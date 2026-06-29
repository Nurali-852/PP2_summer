# Multiple inheritance in Python is a feature that allows a single child class to inherit attributes and methods from more than one parent class

#1
class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming deep!"

# Duck inherits from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    pass

# Usage
donald = Duck()
print(donald.fly())   # Output: Flying high!
print(donald.swim())  # Output: Swimming deep!

#2
class Base:
    def __init__(self):
        print("Base Init")

class Alpha(Base):
    def __init__(self):
        super().__init__()
        print("Alpha Init")

class Beta(Base):
    def __init__(self):
        super().__init__()
        print("Beta Init")

class Combined(Alpha, Beta):
    def __init__(self):
        super().__init__() # Triggers the MRO chain: Combined -> Alpha -> Beta -> Base

obj = Combined()
# Output order: Base Init -> Beta Init -> Alpha Init