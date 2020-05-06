import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 20, 100)
plt.plot(x, 1/x , label='f(x) = 1/x')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.axis([0, 20, 0, 1])
plt.legend()

plt.show()