Programación Entera:

Supongamos que eres un comerciante que desea maximizar sus ganancias al empacar una mochila con diferentes objetos para vender. Tienes cuatro objetos, cada uno con su peso y valor. Los pesos y valores de los objetos se definen como sigue:
•	Objeto A: peso 5 kg, valor $10
•	Objeto B: peso 4 kg, valor $40
•	Objeto C: peso 6 kg, valor $30
•	Objeto D: peso 3 kg, valor $50
Sin embargo, tu mochila tiene un límite de peso máximo de 10 kg.
Utilizando la programación lineal entera, tu objetivo es determinar qué objetos debes seleccionar para maximizar el valor total sin exceder el límite de peso de la mochila.
Escribe un programa en Python utilizando la librería PuLP que resuelva este problema y muestre los objetos seleccionados junto con el valor óptimo alcanzado.
 
- Importamos la biblioteca PuLP para poder utilizar sus funcionalidades de resolución de problemas de programación entera.

- Creamos una lista de objetos que se pueden incluir en la mochila. Cada objeto tiene un peso y un valor asociado.

- Definimos el peso máximo que puede soportar la mochila.

- Creamos un problema de programación lineal entera llamado "Problema_de_la_mochila" con el objetivo de maximizar.

- Creamos una variable binaria para cada objeto utilizando la función LpVariable.dicts de PuLP. Estas variables indicarán si un objeto se incluye (valor 1) o no se incluye (valor 0) en la mochila.

- Definimos la función objetivo, que tiene como objetivo maximizar el valor total de los objetos seleccionados. Esto se logra multiplicando el valor de cada objeto por su variable correspondiente y luego sumando todos estos productos utilizando la función lpSum de PuLP.

- Definimos la restricción del problema, que establece que el peso total de los objetos seleccionados no debe superar el peso máximo de la mochila. Esto se logra multiplicando el peso de cada objeto por su variable correspondiente y luego sumando todos estos productos utilizando la función lpSum de PuLP. Esta suma debe ser menor o igual al peso máximo.

- Resolvemos el problema utilizando el método solve(). Esto encontrará la solución óptima del problema.

- Mostramos el estado de la solución utilizando la función LpStatus, que nos dará información sobre si la solución es óptima, factible, no factible, etc.

- Mostramos los objetos seleccionados y el valor óptimo de la función objetivo. Iteramos sobre las variables del problema y si una variable tiene un valor igual a 1, significa que el objeto correspondiente se ha seleccionado. Imprimimos el nombre del objeto y finalmente imprimimos el valor óptimo de la función objetivo utilizando la función value() de PuLP y pasando como argumento el objeto objective del problema.


Programación Lineal:

Imagina que eres un fabricante de productos y deseas maximizar tus ganancias. Tienes dos productos, producto X y producto Y. Cada producto tiene un costo de producción asociado y puedes venderlos a diferentes precios. Los costos de producción y precios de venta de los productos son los siguientes:
Producto X tiene un costo de producción de $2 y se vende a $5.
Producto Y tiene un costo de producción de $3 y se vende a $4.
Además, tienes dos restricciones en tu producción:
La suma de la cantidad de producto X y producto Y no puede exceder 5.
El costo total de producción (considerando las cantidades de cada producto) no puede exceder $8.
Usando programación lineal, tu objetivo es determinar las cantidades de producto X y producto Y que maximicen tus ganancias.
Escribe un programa en Python utilizando la biblioteca PuLP que resuelva este problema y muestre las cantidades óptimas de producto X y producto Y, así como el valor óptimo de ganancias alcanzado


- Importamos la biblioteca PuLP para poder utilizar sus funcionalidades de resolución de problemas de programación lineal.

- Creamos un problema de programación lineal llamado "Problema_Lineal" con el objetivo de maximizar.

- Definimos las variables de decisión x1 y x2 utilizando la función LpVariable de PuLP. Estas variables son no negativas, ya que se les ha establecido un límite inferior (lowBound=0).

- Definimos la función objetivo, que en este caso es 2x1 + 3x2. Queremos maximizar esta función.

- Definimos las restricciones del problema. En este caso, tenemos dos restricciones: x1 + x2 <= 5 y 2*x1 + x2 <= 8.

- Resolvemos el problema utilizando el método solve(). Esto encontrará la solución óptima del problema.

- Imprimimos el estado de la solución utilizando la función LpStatus, que nos dará información sobre
