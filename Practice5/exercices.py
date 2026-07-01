import re
txt = input()

#1
def zero_more_B():
    x = re.findall("ab*", txt)
    print(x)
#zero_more_B()

#2
def two_three_B():
    x = re.findall(r"ab{2,3}", txt)
    print(x)
#two_three_B()

#3
def Sequence_lower_letters():
    pattern = r"[a-z]+(?:_[a-z]+)+"
    x = re.findall(pattern,txt)
    print(x)
#Sequence_lower_letters()

#4
def Up_low():
    x = re.findall("[A-Z][a-z]", txt)
    print(x)
#Up_low()

#5
def A_B():
    x = re.findall("a.*b$", txt)
    print(x)
#A_B()

#6
def replace():
    x = txt
    pattern = r"[ ,.]"
    print(re.sub(pattern, ":", txt))
#replace()

#7
def snake_to_camel():
    x = txt.split("_")
    for i in range(1, len(x)):
        x[i] = x[i].capitalize()
    for x in x:
        print(x, end="")
#snake_to_camel()

#8
def split_upper():
    x = re.split(r"(?=[A-Z])", txt)
    print(x)
#split_upper()

#9
def split_upper2():
        x = re.sub(r"([A-Z])", r" \1", txt).strip()
        print(x)
#split_upper2()

#10
def camel_to_snake():
    x = re.sub(r"([A-Z])", r"_\1", txt).lower()

    if x.startswith("_"):
        x = x[1:]
    print(x)
#camel_to_snake()