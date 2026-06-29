import math

#1
a = int(input("Degree: "))
b = math.radians(a)
print("Radian:", b)

#2
h = int(input("Height: "))
b1 = int(input("Base 1: "))
b2 = int(input("Base 2: "))

area1 = ((b1 + b2) / 2) * h
print("Area of trapezoiid:", area1)

#3
s = int(input("Number of sides: "))
l = int(input("Length of a side: "))

area2 = (s * l * l) / (4 * math.tan(math.pi / s))
print("Area of a polygon:", int(area2))

#4
x = int(input("Base:"))
y = int(input("Height:"))
print("Area of parallelogram:", float(x * y))