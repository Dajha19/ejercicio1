import matplotlib.pyplot as plt
import numpy as np

# Definir los puntos para la línea punteada
xpoints1 = np.array([0, 1, 2, 3, 4, 5])
ypoints1 = np.array([0, 0, 0, 0, 0, 0])

# Definir los puntos para los cuadrados (serie azul)
x_squares = np.array([0, 1, 2, 3, 4])
y_squares = np.array([0, 1, 4, 9, 16])

# Definir los puntos para los triángulos (serie gris)
x_triangles = np.array([0, 1, 2, 3, 4])
y_triangles = np.array([0, 3, 10, 30, 60])

# Ajustar límites del gráfico
plt.ylim(0, 120)

# Graficar la línea punteada en color gris
plt.plot(xpoints1, ypoints1, linestyle='dotted', color='blue', label='Línea Punteada', marker='v')

# Graficar la serie con cuadrados azules
plt.plot(x_squares, y_squares, 'bs-', label='Serie Cuadrados')

# Graficar la serie con triángulos grises
plt.plot(x_triangles, y_triangles, 'k^--', label='Serie Triángulos')

# Personalizar el gráfico
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico similar a la imagen')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
