from vpython import *

#box(size=vector(1,1,1), pos=vector(0,0,0), color=color.blue)
#box(pos=vector(1,2,3), size=vector(4,5,6))
sprezyna = helix(pos=vector(-5,0,0), axis=vector(1,0,0), size=vector(2.0,0.5,0.5), color=color.green, coils=8, thickness=0.1)
pudelko = box(pos=vector(sprezyna.pos), size=vector(0.5,0.5,0.5), color=color.blue)

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
