import matplotlib.pyplot as plt
import numpy as np

xpoints1 = np.array([1, 4, 5, 6,7])
ypoints1 = np.array([2, 6, 3, 6,3])
plt.ylim (0, 8)

plt.plot(xpoints1, ypoints1, linestyle = 'dotted', marker='o')


plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Líneas Intersectadas')

plt.legend()

plt.show()

