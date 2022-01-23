from math import sin
from vpython import graph, gcurve, gdots, color

def xrange(x1, x2, d):
    while x1 < x2:
        yield x1
        x1 += d

print("Wprowadz wartosc x_min: ", end='')
x_min = int(input())
print("Wprowadz wartosc x_max: ", end='')
x_max = int(input())

data = [(x, sin(x)) for x in xrange(x_min, x_max, 0.1)]
for i in data:
    print(i)