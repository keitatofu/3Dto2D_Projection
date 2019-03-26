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
fig = plt.figure()
ax = plt.axes(xlim =(-1,1),ylim =(-1,1))

#   Declared to allow for x and y axis only
projection = np.array([ [1,0,0], [0,1,0] ])

plt.title("Render 3D Cube in 2D Space")

# list of the angles in radians
angles = np.linspace(0, 2*np.pi, 360)

# storage of single frames - one value per point and angle.
frames = np.zeros((len(load),len(angles),2))

# loops through all points and angles to store for later usage.
for i, x in enumerate(load):
    for j, angle in enumerate(angles):
        rotationY = np.array([[np.cos(angle),0,np.sin(angle)],
                        [0,1,0],
                        [-np.sin(angle),0,np.cos(angle)] ])
        rotationX = np.array([ [1,0,0],
                        [0,np.cos(angle),-np.sin(angle)],
                        [0,np.sin(angle),np.cos(angle)] ])
        rotationZ = np.array([ [np.cos(angle),-np.sin(angle),0], 
                      [np.sin(angle),np.cos(angle),0], 
                      [0,0,1] ])
        rotated = np.dot(rotationX, x)
        rotated = np.dot(rotationY, rotated)
        rotated = np.dot(rotationZ,rotated)
        projected2d = np.dot(projection, rotated)
        print(projected2d)
        # store the point.
        frames[i,j,:] = projected2d

# draws the initial point.
line, = ax.plot(frames[:,0,0], frames[:,0,1], c="blue", marker="o", ls='')


# defines what happens at frame 'i' - you want to update with the current
# frame that we have stored before.
def animate(i):
    line.set_data(frames[:,i,0], frames[:,i,1])
    return line # not really necessary, but optional for blit algorithm

# the number of frames is the number of angles that we wanted.
anim = FuncAnimation(fig, animate, interval=200, frames=len(angles))
plt.draw()
plt.show()


#   Dear Programmers,
#   This code used to be freshly written by me
#   But now only God knows why and what is happening
#   If you see this, tell others about the time I sacrifised
#   Just to do this,    Time taken :    1 whole week
#   Yours Sincere.