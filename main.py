from math import sin
from vpython import graph, gcurve, gdots, color

def xrange(x1, x2, d):
    while x1 < x2:
        yield x1
        x1 += d


def lagrange(nodes, x):
    w = 0
    for i, (xi, f_xi) in enumerate(nodes):
        c = 1
        for j, (xj, f_xj) in enumerate(nodes):
            if j != i:
                c *= (x - xj) / (xi - xj)
        w += f_xi * c
    return w


a = - 10
b = 10
graph(xmin=a, xmax=b, ymin=-1.5, ymax=1.5)

data = [(x, sin(x)) for x in xrange(a, b, 0.1)]
nodes = [(x + 0.4, sin(x + 0.4)) for x in xrange(a, b, 1.5)]
interpolate = [(x, lagrange(nodes, x)) for x in xrange(a, b, 0.1)]
gcurve(data=data, color=color.red)
gdots(data=nodes, color=color.blue)
gcurve(data=interpolate, color=color.green)