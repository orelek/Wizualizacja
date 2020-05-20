import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random



# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    '''
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

markerList = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2',
              '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x', 'X',
              'D', 'd', 4, 5, 6, 7, 8, 9, 10]
colorList = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
randmark = random.choice(markerList)
randcol = random.choice(colorList)
def randPar(x):
    return ( random.choice(colorList), random.choice(markerList), - x * 10 + 20 , - x * 10 )
fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100

# Dla każdego zbioru styli i zakresów wygeneruj n losowych punktów
# zdefiniowane przez x z [23, 32], y in [0, 100], z z [zlow, zhigh].
for c, m, zlow, zhigh in [( randPar(1)), ( randPar(2) ), ( randPar(3) ), ( randPar(4) ), ( randPar(5) )]:
    xs = randrange(n, 0 , 100 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()