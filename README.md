# 3Dto2D_Projection
Create a 3D projected cube in to 2D Cartesian Plane and Animate it using the matplotlib built in python library.

The FuncAnimation constructor takes a callable function (in my case variable called animate) which gets the current frame number as an argument (here i) and updates the plot. This means, all your intermediate points should be stored in an array (frames) and then later access those (possible to also compute the projection on the fly,but not recommended). The animation will then loop through the frames and apply the function to every frame. 


Sources used:

https://en.wikipedia.org/wiki/Rotation_matrix   (Equation for Rotation Matrix).

https://github.com/CodingTrain/website/tree/master/CodingChallenges/CC_112_3D_Rendering/P5  (Javascript Lang.).

https://thecodingtrain.com/CodingChallenges/112-3d-rendering  (Inspiration and what makes me move forward).

https://en.wikipedia.org/wiki/3D_projection.

http://matrixmultiplication.xyz/  (Visualized matrix multiplication).
