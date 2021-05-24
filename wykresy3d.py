import numpy as np
import matplotlib.pyplot as plt

# zad 1

fig = plt.figure()
ax = fig.gca(projection='3d')

z = np.linspace( 0 , 2 * np.pi, 100 )

x = np.sin(z)
y = np.cos(z) * 2
ax.plot(x,y,z, label = 'zadanie 1')
ax.legend()
plt.show()

# zad 2