import math

def pythagoras(a, b):
  c = math.sqrt(a**2 + b**2)
  return c

def circle(r):
  area = math.pi * r**2
  return area

a, b = 3, 4
c = pythagoras(a, b)
print('c =', c)

r = 10
area = circle(r)
print('area =',area)
