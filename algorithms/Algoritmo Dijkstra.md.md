# Algoritmo dijkstra

## Explicacion detallada del problema

Primero se agrupan los puntos de entrega más cercanos a cada almacén y luego se procederá a calcular
los caminos minimos desde cada almacén a cada punto de entrega agrupado previamente.
Por ejemplo: si hay 50 almacenes y 2500 puntos de entrega, aproximadamente le tocará a cada almacen
entregar a 50 puntos de entrega.

Luego para calcular el camino mínimo de cada almacén hacia sus 
aproximadamente 50 puntos de entrega se usará el algoritmo de Dijsktra el cual es el siguiente:
Se inicia poniendo al punto de inicio sin padre y su distancia hacia el mismo punto es 0 pero aun 
no ha recorrido todos los puntos, las distancias hacia los demás puntos es infinito.

Luego se va hacia los puntos de entrega adyacentes se va hacia los caminos adyacentes y se actualiza las distancias de cada punto encolando las
distancias minimas y desencolando cada vez que se encuentra una distancia minima mejor, este algoritmo
termina cuando ha recorrido todos los puntos y se compara entre los caminos generados y se elige el menor

## Posible analisis asintotico

La complejidad computacional del algoritmo de Dijkstra se puede calcular contando las operaciones realizadas:
- El algoritmo consiste en n-1 iteraciones, como máximo. En cada iteración, se añade un vértice al conjunto distinguido.
- En cada iteración, se identifica el vértice con la menor etiqueta . El número de estas operaciones está acotado por n-1.
- Además, se realizan una suma y una comparación para actualizar la etiqueta de cada uno de los vértices que no están en Sk.

Luego, en cada iteración se realizan a lo sumo 2(n-1) operaciones.
