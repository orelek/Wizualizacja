import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
s = np.sin(x)
plt.plot(x, s+2, label='sin(x)')
plt.plot(x, -s, label='sin(x)', color="orange")

plt.xlabel('x')
plt.ylabel('sin(x)')


plt.title("Wykres sin(x),sin(x)")

plt.legend()

plt.show()