import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.arange(-5,6)
y = x ** 2

plt.plot(x,y, label='linia 1/x')
plt.legend()
plt.show()

plt.plot(y, label='linia 1/x')
plt.legend()
plt.show()