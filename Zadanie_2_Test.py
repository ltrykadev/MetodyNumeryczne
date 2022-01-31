import matplotlib.pyplot as plt
import numpy as np

fig, circle = plt.subplots()
draw_circle = plt.Circle((0.0, 0.0), 1, fill=False)

circle.set_xlim(-2, 2)
circle.set_ylim(-2, 2)
circle.set_box_aspect(1)
circle.add_artist(draw_circle)

print("Wprowadz liczbe N: ", end='')
n=int(input())
#x=np.random.rand(n)
#y=np.random.rand(n)
#plt.scatter(x,y)
plt.title('Zadanie 2')
plt.grid(visible=True)

plt.show()