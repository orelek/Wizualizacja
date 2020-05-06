import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 20, 100)

plt.plot(x, 1/x, 'g--', label='f(x)=1/x', marker="^", linewidth=1)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.axis([0, 21, 0, 1])
plt.legend()

plt.show()