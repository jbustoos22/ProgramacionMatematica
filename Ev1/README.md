Importamos la biblioteca NumPy para realizar los cálculos matriciales necesarios.

Definimos la función simplex que toma tres parámetros: c (los coeficientes de la función objetivo), A (las restricciones) y b (los límites o restricciones).

Creamos la tabla inicial utilizando la función hstack de NumPy para combinar las matrices A y b en una sola matriz. También añadimos una matriz identidad utilizando la función eye de NumPy para representar las variables de holgura.

El bucle while se repite hasta que no existan coeficientes negativos en la primera fila de la tabla. Esto significa que hemos alcanzado la solución óptima.

En cada iteración del bucle, determinamos la variable que entra y la variable que sale de la base. La variable que entra es aquella con el coeficiente negativo más pequeño en la primera fila de la tabla (seleccionada con la función argmin de NumPy). Para determinar la variable que sale de la base, calculamos las razones entre los límites (b) y los coeficientes correspondientes en la columna de la variable que entra. Seleccionamos la fila con la razón más pequeña (excluyendo las filas negativas) utilizando nuevamente la función argmin de NumPy.

Actualizamos la tabla dividiendo la fila seleccionada por el pivot (el elemento en la intersección de la fila y la columna de la variable que entra).

Luego, realizamos operaciones de fila y columna para obtener una nueva tabla, manteniendo la columna de la variable que entra igual a 0 y actualizando el resto de los elementos según las operaciones de pivote.

Al final del bucle, obtenemos la solución óptima tomando el valor óptimo de la celda en la primera fila y primera columna de la tabla y la solución correspondiente en las filas restantes.

Finalmente, imprimimos la solución óptima y el valor óptimo utilizando la función print.