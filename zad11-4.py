import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure( figsize =( plt.figaspect( 0.15 )))
ax1 = fig.add_subplot( 151 , projection = '3d' )
ax2 = fig.add_subplot( 152 , projection = '3d' )
ax3 = fig.add_subplot( 153 , projection = '3d' )
ax4 = fig.add_subplot( 154 , projection = '3d' )
ax5= fig.add_subplot( 155 , projection = '3d' )
# fikcyjne dane
_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
ax1.set_title('Wykres 1')
ax2.bar3d(x, y, top, width, depth, bottom, color = 'r', shade = True )
ax2.set_title('Wykres 2')
ax3.bar3d(x, y, bottom, width, depth, top, color = 'g')
ax3.set_title('Wykres 3')
ax4.bar3d(2 * x, 3 * y, bottom, width, depth, top, shade = False)
ax4.set_title('Wykres 4')
ax5.bar3d(2 * x,1.5 * y, bottom, width, depth, top, color = 'b', shade = True )
ax5.set_title('Wykres 5')

plt.show()