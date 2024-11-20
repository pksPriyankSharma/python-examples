# example of using numpy with Matplot libraries
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 100)
sinx = np.sin(x)
plt.plot(x, sinx)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sine Wave")
plt.xlim([0, 4*np.pi])
plt.ylim([-1.5,1.5])
plt.show()