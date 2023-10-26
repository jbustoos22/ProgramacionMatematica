# Definimos una función llamada esquina_noroeste para hacer los cálculos
def esquina_noroeste(costos, capacidad, requerimientos):
    # Creamos una matriz para almacenar la asignación de recursos.
    asignacion = [[0 for _ in range(len(requerimientos))] for _ in range(len(capacidad))]
    
    # Variables para rastrear los índices de capacidad y requerimientos.
    i = 0
    j = 0
    
    # Variable para almacenar el costo total de la asignación.
    total_costo = 0

    # Realizamos la asignación siguiendo el algoritmo de la esquina noroeste.
    while i < len(capacidad) and j < len(requerimientos):
        # Calculamos el mínimo entre la capacidad en i y el requerimiento en j.
        minimo = min(capacidad[i], requerimientos[j])
        
        # Asignamos el mínimo en la posición correspondiente de la matriz asignación.
        asignacion[i][j] = minimo
        
        # Añadimos el costo de esta asignación al costo total.
        total_costo += minimo * costos[i][j]
        
        # Reducimos la capacidad y el requerimiento en función del mínimo asignado.
        capacidad[i] -= minimo
        requerimientos[j] -= minimo

        # Verificamos si se agotó la capacidad en i y avanzamos al siguiente índice.
        if capacidad[i] == 0:
            i += 1
        
        # Verificamos si se cumplió el requerimiento en j y avanzamos al siguiente índice.
        if requerimientos[j] == 0:
            j += 1

    # Devolvemos la matriz asignación que contiene la asignación de recursos y el costo total.
    return asignacion, total_costo

# Datos de ejemplo
costos = [[10, 7, 5, 12], [6, 2, 9, 11], [8, 6, 4, 14]]
capacidad = [20, 30, 10]
requerimientos = [15, 25, 20, 10]

# Llamamos a la función esquina_noroeste para obtener la asignación de recursos y el costo total.
asignacion, total_costo = esquina_noroeste(costos, capacidad, requerimientos)

# Imprimimos las asignaciones realizadas.
print("Asignaciones realizadas:")
for i in range(len(asignacion)):
    print("Capacidad ", i, " asignada a: ")
    for j in range(len(asignacion[i])):
        if asignacion[i][j] > 0:
            print("Requerimiento ", j, ": ", asignacion[i][j])

# Imprimimos el costo total de la asignación.
print("Costo total de la asignación: ", total_costo)

