from vpython import *

scene.width = 1000
scene.height = 1000
scene.title = "Metody numeryczne - Łukasz Tryka - 17812"
scene.camera.pos = vector(1.5, 0.5, 8.5)
scene.camera.axis = vector(-1.5, -0.5, -8.5)

stiffness_initial = float(input("Wprowadz wartość poczatkową tłumienia np. 1.0: "))
springiness_initial = float(input("Wprowadz wartość poczatkową sprężystości np. 0.1: "))
position_initial = float(input("Wprowadz wartość poczatkową wychylenia np. 0.0: "))
speed_initial = float(input("Wprowadz wartość poczatkową prędkości np. 1.0: "))

sciana1 = box(pos=vector(-3.0, 0.0, 0.0), size=vector(0.5, 3.0, 3.0), color=color.red)  # lewa
sciana2 = box(pos=vector(0.0, 0.0, -1.25), size=vector(6.5, 3.0, 0.5), color=color.red) # tylna
sciana3 = box(pos=vector(3.0, 0.0, 0.0), size=vector(0.5, 3.0, 3.0), color=color.red)   # prawa
podloga = box(pos=vector(0.0, -1.5, 0.0), size=vector(6.5, 0.5, 3.0), color=color.red)
sufit = box(pos=vector(0.0, 1.5, 0.0), size=vector(6.5, 0.5, 3.0), color=color.red)
pudelko = box(pos=vector(position_initial, 0.0, 0.0), size=vector(1.0, 1.0, 1.0), color=color.yellow, weight=1.0, speed=vector(speed_initial, 0.0, 0.0), leave_matrix=0)
sprezyna = helix(pos=vector(-2.75, 0.0, 0.0), axis=vector(0.0, 0.0, 0.0), radius=0.2, thickness=0.2, coils=10, color=color.green, stiffness=stiffness_initial, springiness=springiness_initial)

scene.append_to_caption('Zakończyć symulację ? \n')
def Menu(m):
    if m.selected == 'TAK':
        pudelko.leave_matrix = 1
menu(choices=['NIE', 'TAK'], bind=Menu)
scene.append_to_caption('\n\n')

scene.append_to_caption('Pokazać obiekt ściana1? ')
def Menu(s1):
    if s1.selected == 'TAK':
        sciana1.size = vector(0.5, 3.0, 3.0)
    else:
        sciana1.size = vector(0.0, 0.0, 0.0)
menu(choices=['TAK', 'NIE'], bind=Menu)
scene.append_to_caption('\n')

scene.append_to_caption('Pokazać obiekt ściana2? ')
def Menu(s2):
    if s2.selected == 'TAK':
        sciana2.size = vector(6.5, 3.0, 0.5)
    else:
        sciana2.size = vector(0.0, 0.0, 0.0)
menu(choices=['TAK', 'NIE'], bind=Menu)
scene.append_to_caption('\n')

scene.append_to_caption('Pokazać obiekt ściana3? ')
def Menu(s3):
    if s3.selected == 'TAK':
        sciana3.size = vector(0.5, 3.0, 3.0)
    else:
        sciana3.size = vector(0.0, 0.0, 0.0)
menu(choices=['TAK', 'NIE'], bind=Menu)
scene.append_to_caption('\n')

scene.append_to_caption('Pokazać obiekt podłoga? ')
def Menu(p):
    if p.selected == 'TAK':
        podloga.size = vector(6.5, 0.5, 3.0)
    else:
        podloga.size = vector(0.0, 0.0, 0.0)
menu(choices=['TAK', 'NIE'], bind=Menu)
scene.append_to_caption('\n')

scene.append_to_caption('Pokazać obiekt sufit? ')
def Menu(su):
    if su.selected == 'TAK':
        sufit.size = vector(6.5, 0.5, 3.0)
    else:
        sufit.size = vector(0.0, 0.0, 0.0)
menu(choices=['TAK', 'NIE'], bind=Menu)
scene.append_to_caption('\n')

dt = 0.01
punkt_rownowagi = vector(0.0, 0.0, 0.0)

while (pudelko.leave_matrix == 0):
    rate(500)

    krok1_x = punkt_rownowagi - pudelko.pos
    krok1_v = pudelko.speed
    krok1_a = -1 * (((sprezyna.springiness / pudelko.weight) * krok1_v) - ((sprezyna.stiffness / pudelko.weight) * krok1_x))
    krok2_x = krok1_x + krok1_v * (1/2 * dt)
    krok2_v = krok1_v + krok1_a * (1/2 * dt)
    krok2_a = -1 * (((sprezyna.springiness / pudelko.weight) * krok2_v) - ((sprezyna.stiffness / pudelko.weight) * krok2_x))
    krok3_x = krok1_x + krok2_v * (1/2 * dt)
    krok3_v = krok1_v + krok2_a * (1/2 * dt)
    krok3_a = -1 * (((sprezyna.springiness / pudelko.weight) * krok3_v) - ((sprezyna.stiffness / pudelko.weight) * krok3_x))
    krok4_x = krok1_x + krok3_v * dt
    krok4_v = krok1_v + krok3_a * dt
    krok4_a = -1 * (((sprezyna.springiness / pudelko.weight) * krok4_v) - ((sprezyna.stiffness / pudelko.weight) * krok4_x))

    pudelko.pos = pudelko.pos + 1/6 * (krok1_v + 2 * krok2_v + 2 * krok3_v + krok4_v) * dt
    sprezyna.axis = pudelko.pos - sprezyna.pos - vector(0.5, 0.0, 0.0)

    pudelko.speed = pudelko.speed + krok4_a * dt

    print(scene.camera.pos)
    print(scene.camera.axis)
