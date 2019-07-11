import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
from mpl_toolkits.mplot3d import axes3d

x = z = np.linspace(-100,100,256)
x , z = np.meshgrid(x,z)
y = (255 - imread('/home/lun/ピクチャ/python.png')*255) * 10

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(np.ravel(x), np.ravel(z), np.ravel(y),s=10,marker='.')
ax.set_title("image")
plt.show()

