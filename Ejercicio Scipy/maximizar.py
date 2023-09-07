import numpy as np
from scipy.optimize import linprog

# Coeficientes de la función objetivo a maximizar (-Z)
c = [-2, -1]

# Coeficientes de las restricciones de desigualdad (Ax ≤ b)
A = [
    [1, 1],
    [2, 1]
]

# Lado derecho de las restricciones de desigualdad
b = [8, 12]

# Límites para las variables (x, y)
x_bounds = (0, None)
y_bounds = (0, None)

# Resolver el problema de programación lineal utilizando el método Simplex
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

if result.success:
    x_optimal, y_optimal = result.x
    optimal_value = -result.fun  # Convertir de vuelta al valor de maximización actual

    print("Solución óptima:")
    print(f"x = {x_optimal}")
    print(f"y = {y_optimal}")
    print(f"Valor óptimo de Z: {optimal_value}")
else:
    print("La optimización no tuvo éxito. Verifica la formulación del problema.")
