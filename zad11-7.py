from numpy.random import rand
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import get_test_data


fig = plt.figure()

ax = fig.add_subplot( 1 , 1 , 1 , projection = '3d' )
x = rand(5)
y = rand(5)
z = rand(5)
ax.plot(x, y, z, color = 'g')


m = rand(20, 3)
for i in range(len(m)):
    x = m[i, 0]
    y = m[i, 1]
    z = m[i, 2]
    ax.scatter(x, y, z, color='r')

for angle in range(0, 360):
    plt.draw()
    plt.pause(.001)
plt.show()