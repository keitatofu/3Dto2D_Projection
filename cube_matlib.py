import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = np.array([-0.5,-0.5,-0.5])
B = np.array([0.5,-0.5,-0.5])
C = np.array([0.5,0.5,-0.5])
D = np.array([-0.5,0.5,-0.5])
E = np.array([-0.5,-0.5,0.5])
F = np.array([0.5,-0.5,0.5])
G = np.array([0.5,0.5,0.5])
H = np.array([-0.5,0.5,0.5])

load = np.array([A,B,C,D,E,F,G,H])
print(load)

fig = plt.figure()
ax = plt.axes(xlim =(-1,1),ylim =(-1,1))

#	Declared to allow for x and y axis only
projection = np.array([ [1,0,0], [0,1,0] ])

plt.title("Render 3D Cube in 2D Space")
for x in load:
	for angle in range(360):
		rotationY = np.array([ [np.cos(angle),0,np.sin(angle)],
					   	[0,1,0],
					   	[-np.sin(angle),0,np.cos(angle)] ])
		rotationX = np.array([ [1,0,0],
 					   	[0,np.cos(angle),-np.sin(angle)],
 					   	[0,np.sin(angle),np.cos(angle)] ])
		
		#	Drawing each points
		rotated = np.dot(rotationY,x)
		rotated = np.dot(rotationX,rotated)
		projected2d = np.dot(projection,rotated)
		#projected2d = np.dot(projection,x)	-With no rotations
	ax.plot(projected2d[0],projected2d[1],c = "blue",marker = "o")[0]

plt.grid()
#plt.draw()
plt.show()


# rotationZ = np.array([ [np.cos(angle),-np.sin(angle),0], 
# 					    [np.sin(angle),np.cos(angle),0], 
# 					    [0,0,1] ])
# rotationY = np.array([ [np.cos(angle),0,np.sin(angle)],
# 					   	[0,1,0],
# 					   	[-np.sin(angle),0,np.cos(angle)] ])
# rotationX = np.array([ [1,0,0],
# 					   	[0,np.cos(angle),-np.sin(angle)],
# 					   	[0,np.sin(angle),np.cos(angle)] ])
