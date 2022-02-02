from vpython import *
#scene = display(title='Examples of Tetrahedrons', x=0, y=0, width=600, height=200, center=(5,0,0), background=(0,1,1))
sciana = box(pos=vector(-3,0,0), size=vector(0.5,3.0,3.0), color=color.red)
pudelko = box(pos=vector(0,0,0), size=vector(1.0,1.0,1.0), color=color.yellow, weight=1.0, speed=vector(1,0,0))
sprezyna = helix(pos=vector(-2.75,0,0), axis=vector(2,0,0), radius=0.2, thickness=0.2, coils=10, color=color.green, stiffness=1.0, springiness=0.1)
punkt_rownowagi = vector(0,0,0)
time = 0.1

while (True):
    rate(60)

    krok1_x = punkt_rownowagi - pudelko.pos
    krok1_v = pudelko.speed
    krok1_a = krok1_x * (sprezyna.stiffness / pudelko.weight) - (sprezyna.springiness / pudelko.weight) * krok1_v

    krok2_x = krok1_x + krok1_v * (0.5 * time)
    krok2_v = krok1_v + krok1_a * (0.5 * time)
    krok2_a = krok2_x * (sprezyna.stiffness / pudelko.weight) - (sprezyna.springiness / pudelko.weight) * krok2_v

    krok3_x = krok2_x + krok2_v * (0.5 * time)
    krok3_v = krok2_v + krok2_a * (0.5 * time)
    krok3_a = krok3_x * (sprezyna.stiffness / pudelko.weight) - (sprezyna.springiness / pudelko.weight) * krok3_v

    krok4_x = krok3_x + krok3_v * time
    krok4_v = krok3_v + krok3_a * time
    krok4_a = krok4_x * (sprezyna.stiffness / pudelko.weight) - (sprezyna.springiness / pudelko.weight) * krok4_v

    pudelko.pos = pudelko.pos + time * (krok1_v + 2 * krok2_v + 2 * krok3_v + krok4_v) / 6
    sprezyna.axis = pudelko.pos - sprezyna.pos - vector(0.5, 0.0, 0.0)
    pudelko.speed = pudelko.speed + time * (krok1_a + 2 * krok2_a + 2 * krok3_a + krok4_a) / 6

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
