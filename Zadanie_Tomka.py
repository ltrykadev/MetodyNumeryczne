from vpython import *
from IPython.display import display

display(witdth=600, height=600, center=vector(6, 0, 0), background=color.white)
wall = box(pos=vector(0, 1, 0), size=vector(0, 2, 3), color=color.green)
mass = box(pos=vector(float(input('Initial displacement: ')), 0, 0), velocity=vector(float(input('Initial velocity: ')), 0, 0), size=vector(1, 1, 1), mass=5.0, color=color.blue)
pivot = vector(0, 0, 0)
spring = helix(pos=pivot, axis=Mass.pos - pivot, radius=0.4, constant=float(input('spring constant: ')), damping=float(input('damping constant: ')), thickness=0.1, coils=20, color=color.red)

eq = vector(9, 0, 0)  # equlibrium
marker_equilbrium = arrow(pos=vector(9, -2.5, 0), axis=vector(0, 2, 0), shaftwidth=0.1,shaftlength=0.5, color=color.red)

t = 0
dt = 0.01
while (t < 200):
    rate(60)
    k1x = eq - Mass.pos
    k1v = Mass.velocity
    k1acc = (eq - Mass.pos) * (spring.constant / Mass.mass) - (spring.damping / Mass.mass) * Mass.velocity

    k2x = k1x + k1v * (dt / 2)
    k2v = k1v + k1acc * (dt / 2)
    k2acc = k2x * (spring.constant / Mass.mass) - (spring.damping / Mass.mass) * k2v

    k3x = k2x + k2v * (dt / 2)
    k3v = k2v + k2acc * (dt / 2)
    k3acc = k3x * (spring.constant / Mass.mass) - (spring.damping / Mass.mass) * k3v

    k4x = k3x + k3v * (dt / 2)
    k4v = k3v + k3acc * (dt / 2)
    k4acc = k3x * (spring.constant / Mass.mass) - (spring.damping / Mass.mass) * k3v

    Mass.pos = Mass.pos + dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
    Mass.velocity = Mass.velocity + dt * (k1acc + 2 * k2acc + 2 * k3acc + k4acc) / 6

    spring.axis = Mass.pos - spring.pos
    t = t + dt