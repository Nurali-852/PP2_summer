import datetime as d

#1 
x = d.datetime.now()
y = x - d.timedelta(days = 5)
print(y)

#2
x = d.date.today()
y = x - d.timedelta(days = 1)
z = x + d.timedelta(days = 1)

print("Yesterday:", y)
print("Today:", x)
print("Tomorrow:", z)

#3
x = d.datetime.now()
print(x.strftime("%Y-%m-%d %H:%M:%S"))

#4
x = d.datetime.now()
x = x.replace(microsecond = 0)
y = d.datetime(2026, 3, 15, 14, 0, 15)
delta = x - y
print(abs(delta.total_seconds()))