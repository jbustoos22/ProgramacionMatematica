# Importar la biblioteca PuLP
import pulp
# Crear el problema de programación lineal
prob = pulp.LpProblem("Problema_Lineal", pulp.LpMaximize)
# Definir las variables de decisión
x1 = pulp.LpVariable("x1", lowBound=0)  # Variable x1 no negativa
x2 = pulp.LpVariable("x2", lowBound=0)  # Variable x2 no negativa
# Definir la función objetivo
prob += 2*x1 + 3*x2, "Función Objetivo: 2x1 + 3x2"
# Definir las restricciones
prob += x1 + x2 <= 5, "Restricción 1: x1 + x2 <= 5"
prob += 2*x1 + x2 <= 8, "Restricción 2: 2x1 + x2 <= 8"
# Resolver el problema
prob.solve()
# Imprimir el estado de la solución
print("Estado:", pulp.LpStatus[prob.status])
# Imprimir los valores de las variables de decisión
for variable in prob.variables():
    print(f"{variable.name}: {variable.varValue}")
# Imprimir el valor óptimo de la función objetivo
print("Valor óptimo de la función objetivo:", pulp.value(prob.objective))
