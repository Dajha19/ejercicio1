import matplotlib.pyplot as plt
import numpy as np

xpoints1 = np.array([10, 20, 30])
ypoints1 = np.array([20, 40, 10])

xpoints2 = np.array([10, 20, 30])
ypoints2 = np.array([40, 10, 30])

plt.plot(xpoints1, ypoints1, label='Line 1', marker='o')

plt.plot(xpoints2, ypoints2, label='Line 2', marker='o')

plt.xlabel('X Points')
plt.ylabel('Y Points')
plt.title('Plot of Two Lines')

plt.legend()
plt.show()
