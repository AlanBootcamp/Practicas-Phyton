import numpy as np
import matplotlib.pyplot as plt

# Función para simular la caída de las canicas
def simular_maquina_galton(num_canicas, num_niveles):
    resultados = np.zeros(num_canicas)  # Array para almacenar el número de caídas a la derecha
    for i in range(num_canicas):
        # Para cada canica, simulamos 12 niveles donde en cada uno se decide aleatoriamente si cae a la izquierda (0) o derecha (1)
        resultados[i] = np.sum(np.random.randint(0, 2, num_niveles))
    return resultados

# Función para graficar el histograma de los resultados
def graficar_histograma(resultados, num_niveles):
    plt.hist(resultados, bins=np.arange(-0.5, num_niveles + 1.5, 1), edgecolor='black')
    plt.title('Simulación de la Máquina de Galton')
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de canicas')
    plt.xticks(range(num_niveles + 1))  # Para que los ticks del eje X coincidan con el número de caídas
    plt.show()

# Parámetros
num_canicas = 3000
num_niveles = 12

# Simulación y graficación
resultados = simular_maquina_galton(num_canicas, num_niveles)
graficar_histograma(resultados, num_niveles)