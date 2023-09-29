'''
El enunciado del ejercicio es el siguiente:

Se desea maximizar la función 40*X1 + 18*X2, sujeta a las siguientes restricciones:

1. 16*X1 + 2*X2 <= 700
2. 6*X1 + 3*X2 <= 612
3. X1 <= 80
4. X2 <= 120
'''

import matplotlib.pyplot as plt  # Importar la biblioteca para graficar
import numpy as np  # Importar la biblioteca para realizar cálculos numéricos
from pulp import LpMaximize, LpProblem, LpStatus, LpVariable  # Importar la biblioteca Pulp

# Crear el problema
prb = LpProblem("Problema de Programación Lineal", LpMaximize)

# Definir las variables de decisión
X1 = LpVariable("X1", lowBound=0)  # Variable de decisión X1 con límite inferior de cero
X2 = LpVariable("X2", lowBound=0)  # Variable de decisión X2 con límite inferior de cero

# Definir la función objetivo
prb += 40*X1 + 18*X2, "ZMAX"  # Función objetivo: maximizar 40*X1 + 18*X2

# Definir las restricciones
prb += 16*X1 + 2*X2 <= 700, "Restricción 1"  # Restricción: 16*X1 + 2*X2 <= 700
prb += 6*X1 + 3*X2 <= 612, "Restricción 2"  # Restricción: 6*X1 + 3*X2 <= 612
prb += X1 <= 80, "Restricción 3"  # Restricción: X1 <= 80
prb += X2 <= 120, "Restricción 4"  # Restricción: X2 <= 120

# Resolver el problema
prb.solve()

# Imprimir el estado de la solución
print("Estado: ", LpStatus[prb.status])

# Imprimir los valores de las variables de decisión
for variable in prb.variables():
    print(variable.name, "=", variable.varValue)

# Imprimir el valor de la función objetivo
print("Valor de la función objetivo: ", prb.objective.value())

# Crear la gráfica
x = np.linspace(0, 80, 100)  # Generar valores para X1 en el intervalo [0, 80]
y = (700 - 16*x) / 2  # Calcular los valores de X2 para la restricción 1

# Graficar las restricciones
plt.plot(x, y, label='Restricción 1')  # Graficar la restricción 1

x = np.linspace(0, 80, 100)  # Generar valores para X1 en el intervalo [0, 80]
y = (612 - 6*x) / 3  # Calcular los valores de X2 para la restricción 2

plt.plot(x, y, label='Restricción 2')  # Graficar la restricción 2

x = np.linspace(0, 80, 100)  # Generar valores para X1 en el intervalo [0, 80]
y = np.minimum(120, x*0)  # Calcular los valores de X2 para la restricción 3

plt.plot(x, y, label='Restricción 3')  # Graficar la restricción 3

x = np.linspace(0, 120, 100)  # Generar valores para X2 en el intervalo [0, 120]
y = np.minimum(80, x*0)  # Calcular los valores de X1 para la restricción 4

plt.plot(y, x, label='Restricción 4')  # Graficar la restricción 4

# Graficar la región factible
x = np.linspace(0, 80, 100)  # Generar valores para X1 en el intervalo [0, 80]
y = np.minimum((700 - 16*x) / 2, (612 - 6*x) / 3)  # Calcular los valores de X2 para la región factible

plt.fill_between(x, 0, y, alpha=0.2, label='Región Factible')  # Rellenar el área de la región factible

# Personalizar la gráfica
plt.xlabel('X1')  # Etiqueta del eje X
plt.ylabel('X2')  # Etiqueta del eje Y
plt.title('Gráfica del Problema')  # Título de la gráfica
plt.legend()  # Agregar leyenda

# Mostrar la gráfica
plt.show()
