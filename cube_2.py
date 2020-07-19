'''
Title: cube_2.py
Author: Roid Maulana
Description: Demonstrating Python Libraries to produce vertices of a cube with rotational animation
             Feel free to improve by forking this repository and submitting pull requests if needed. Happy hacking :)
License:  GNU GENERAL PUBLIC LICENSE 3.0
'''

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

'''
The FuncAnimation constructor takes a callable function (in my case variable called animate) which 
gets the current frame number as an argument (here i) and updates the plot.
This means, all of the intermediate points should be stored in an array (frames) 
and then later access them (possible to also compute the projection on the fly,but not recommended).
The animation will then loop through the frames and apply the function to every frame.
'''
