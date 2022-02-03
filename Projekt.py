from vpython import *

#my_box = box(pos=vector(0,0,0), size=vector(1,1,1), color=color.red)
#scene.append_to_caption('Box Color\n')
#def Menu(m):
#    if m.selected == "red":
#        my_box.color = color.red
#    elif m.selected == "blue":
#        my_box.color = color.blue
#    else:
#        my_box.color = color.green
#menu( choices=['red' ,'blue', 'green'], bind=Menu )
#scene.append_to_caption('\n\n')
#scene = display(title='Examples of Tetrahedrons', x=0, y=0, width=600, height=200, center=(5,0,0), background=(0,1,1))


stiffness_initial = float(input("Wprowadz wartość poczatkową tłumienia np. 1.0: "))
springiness_initial = float(input("Wprowadz wartość poczatkową sprężystości np. 0.1: "))
position_initial = float(input("Wprowadz wartość poczatkową wychylenia np. 0.0: "))
speed_initial = float(input("Wprowadz wartość poczatkową prędkości np. 1.0: "))

sciana = box(pos=vector(-3.0,0.0,0.0), size=vector(0.5,3.0,3.0), color=color.red)
pudelko = box(pos=vector(position_initial,0.0,0.0), size=vector(1.0,1.0,1.0), color=color.yellow, weight=1.0, speed=vector(speed_initial,0.0,0.0))
sprezyna = helix(pos=vector(-2.75,0.0,0.0), axis=vector(0.0,0.0,0.0), radius=0.2, thickness=0.2, coils=10, color=color.green, stiffness=stiffness_initial, springiness=springiness_initial)
punkt_rownowagi = vector(0,0,0)

dt = 0.01

while (True):
    rate(100)

    krok1_x = punkt_rownowagi - pudelko.pos
    krok1_v = pudelko.speed
    krok1_a = krok1_x * (sprezyna.stiffness / pudelko.weight) - (sprezyna.springiness / pudelko.weight) * krok1_v

    krok2_x = krok1_x + krok1_v * (1/2 * dt)
    krok2_v = krok1_v + krok1_a * (1/2 * dt)
    krok2_a = krok2_x * (sprezyna.stiffness / pudelko.weight) - (sprezyna.springiness / pudelko.weight) * krok2_v

    krok3_x = krok1_x + krok2_v * (1/2 * dt)
    krok3_v = krok1_v + krok2_a * (1/2 * dt)
    krok3_a = krok3_x * (sprezyna.stiffness / pudelko.weight) - (sprezyna.springiness / pudelko.weight) * krok3_v

    krok4_x = krok1_x + krok3_v * dt
    krok4_v = krok1_v + krok3_a * dt
    krok4_a = krok4_x * (sprezyna.stiffness / pudelko.weight) - (sprezyna.springiness / pudelko.weight) * krok4_v

    pudelko.pos = pudelko.pos + 1/6 * (krok1_v + 2 * krok2_v + 2 * krok3_v + krok4_v) * dt
    sprezyna.axis = pudelko.pos - sprezyna.pos - vector(0.5, 0.0, 0.0)
    pudelko.speed = pudelko.speed + 1/6 * (krok1_a + 2 * krok2_a + 2 * krok3_a + krok4_a) * dt
