import numpy as np
import matplotlib.pyplot as plt
from math import *

# zad 2 ala 1

# x = np.arange(20,41,0.8)
# plt.plot(x, 1/x, 'bo', x, 1/x, 'b--', label="f(x) = 1/x")
# plt.axis(xmin=20,xmax=40,ymin=0.02,ymax=0.05)
# plt.title('Jakiś wykres')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.show()

# zad 3

x = np.arange(np.pi,46,0.1)
y1 = np.sin(x)
y2 = np.cos(x) # asfias90f8as0f9
plt.plot(x, y1, 'r', x, y2, 'b')
plt.axis(xmin=0,xmax=45,ymin=-1,ymax=3)
plt.show()