import numpy as np
import matplotlib.pyplot as plt

ts_length = 10
e_values = []
i = 0

while i < ts_length:
    e = np.random.randn()
    e_values.append(e)
    i = i + 1

plt.plot(e_values)
plt.show()
