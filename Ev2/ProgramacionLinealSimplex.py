# Una panadería produce dos tipos de pasteles: pastel de chocolate y pastel de fresa. Para la producción de estos pasteles, la panadería necesita utilizar dos ingredientes principales: harina y azúcar.
# Cada pastel de chocolate requiere 2 tazas de harina y 1 taza de azúcar, mientras que cada pastel de fresa necesita 1 taza de harina y 1.5 tazas de azúcar.
# La panadería tiene un límite diario de 10 tazas de harina y 12 tazas de azúcar disponibles. Además, hay una demanda diaria de al menos 5 pasteles de chocolate y 4 pasteles de fresa.
# El objetivo de la panadería es maximizar sus ganancias diarias. El pastel de chocolate se vende a $4 cada uno y el pastel de fresa se vende a $5 cada uno.

import numpy as np

def simplex(c, A, b):
    # Crear la tabla inicial
    table = np.hstack((A, np.eye(len(A))))
    table = np.hstack((table, b.reshape(len(b), 1)))
    # Concatenamos la matriz A con una matriz identidad para las variables de holgura y luego con la matriz b para formar la tabla.

    # Encontrar la variable que entra y la variable que sale de la base
    while np.min(table[0, :-1]) < 0:
        # Si hay coeficientes negativos en la fila objetivo, continuamos iterando
        col = np.argmin(table[0, :-1])
        # Encontramos la columna con el coeficiente negativo más pequeño en la fila objetivo

        ratios = np.where(table[1:, col] > 0, table[1:, -1] / table[1:, col], np.inf)
        # Calculamos las razones entre los límites (b) y los coeficientes de la columna de la variable que entra
        # Si el coeficiente es negativo, asignamos infinito para que no sea considerado

        row = np.argmin(ratios) + 1
        # Encontramos la fila con la razón más pequeña (excluyendo las filas negativas) para determinar la variable que sale

        pivot = table[row, col]
        # Obtenemos el elemento de pivote, que es el coeficiente en la intersección de la fila y la columna de la variable que sale

        table[row, :] /= pivot
        # Dividimos la fila de pivote por el elemento de pivote para hacer que el elemento de pivote sea 1

        for r in range(table.shape[0]):
            if r != row:
                factor = table[r, col]
                table[r, :] -= table[row, :] * factor
                # Realizamos operaciones de fila y columna para actualizar el resto de la tabla

    return table[0, 1:], table[1:, -1]
    # Devolvemos la solución óptima (valores en la primera fila y primera columna) y la solución correspondiente en las filas restantes


# Ejecutamos la función con los datos dados
c = np.array([4, 5])
A = np.array([[2, 1], [1, -3]])
b = np.array([10, 12])

result, solution = simplex(c, A, b)
print("Solución óptima: ", solution)
print("Valor óptimo: ", result)
