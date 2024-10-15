import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

def source(freq, x, x0, y, y0, z, z0):
    radius = np.sqrt((x - x0)**2 + (y - y0)**2 + (z - z0)**2)
    return np.sin(2 * np.pi * freq * radius)


x_size = y_size = 100
z_size = 1000

amps = np.zeros((x_size, y_size, z_size))
for x in tqdm(range(x_size)):
    for y in range(y_size):
        for z in range(z_size):
            amps[x, y, z] += source(0.5, x, 0, y, 0, z, 0)**2 + source(0.5, x, 0, y,y_size, z, 0)**2+source(0.5, x, x_size, y, 0, z, 0)**2+source(0.5, x, x_size, y, y_size, z, 0)**2+source(0.5, x, x_size//2, y, y_size, z, 0)**2+source(0.5, x, x_size, y, y_size//2, z, 0)**2+source(0.5, x, x_size//2, y, 0, z, 0)**2+source(0.5, x, 0, y, y_size//2, z, 0)**2

mini = np.min(amps)
maxi = np.max(amps)

#print("plotting........")
fig = plt.figure()
n = 1  
ax = fig.add_subplot(111, projection='3d')
norm = Normalize(vmin=mini, vmax=maxi)


cmap = plt.get_cmap('coolwarm')


colors = cmap(norm(amps))
alpha = 0.5  
colors[..., 3] = alpha  


ax.voxels(amps[::n, ::n, ::n] , facecolors=colors[::n, ::n, ::n], edgecolor='none')


ax.set(xlabel="X", ylabel="Y", zlabel="Z")
ax.view_init(elev=45, azim=45)

mappable = cm.ScalarMappable(norm=norm, cmap=cmap)
mappable.set_array([])
cbar = fig.colorbar(mappable, ax=ax, shrink=0.5, aspect=10)
cbar.set_label("amplitude")

plt.show()
