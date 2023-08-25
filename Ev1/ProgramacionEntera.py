# Importar la librería PuLP
import pulp
 # Crear una lista de objetos con su peso y valor 
objetos = ["a", "b", "c", "d"] 
pesos = {"a": 5, "b": 4, "c": 6, "d": 3} 
valores = {"a": 10, "b": 40, "c": 30, "d": 50} 
# Crear una variable para el peso máximo de la mochila 
peso_maximo = 10 
# Crear un problema de programación lineal entera
prob = pulp.LpProblem("Problema_de_la_mochila", pulp.LpMaximize) 
# Crear una variable binaria para cada objeto 
x = pulp.LpVariable.dicts("x", objetos, 0, 1, pulp.LpInteger) 
# Definir la función objetivo: maximizar el valor total de los objetos 
prob += pulp.lpSum([valores[i] * x[i] for i in objetos]), "Valor total"
 # Definir la restricción: el peso total de los objetos no debe superar el peso máximo 
prob += pulp.lpSum([pesos[i] * x[i] for i in objetos]) <= peso_maximo, "Peso total" 
# Resolver el problema 
prob.solve()
 # Mostrar el estado de la solución print("Estado:", LpStatus[prob.status]) 
# Mostrar los objetos seleccionados y el valor óptimo 
print("Objetos seleccionados:") 
for v in prob.variables():
    if v.varValue == 1:
        print(v.name) 
print("Valor óptimo:", pulp.value(prob.objective))
