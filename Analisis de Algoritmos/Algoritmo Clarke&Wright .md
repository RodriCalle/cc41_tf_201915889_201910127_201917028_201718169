# Restricciones

El problema de enrutamiento vehicular propone optimizar las rutas para una flota de vehiculos que debe satisfacer las demandas de un conjunto de clientes, minimizando costos de tiempo y distancia para cada vehiculo, entonces se tiene que: 

1. Todos los vehiculos inician y finalizan en el deposito;
2. Cada lugar de entrega es visitado una unica vez por un solo vehículo;
3. Se tiene que cumplir con la capacidad máxima del vehículo y la distancia de viaje;

## Pseudocódigo

El problema de enrutamiento vehicular puede llegar a ser muy complejo y con muchas posibles soluciones, por ello planteare la solucion de la forma mas simple tomando como ejemplo el algoritmo de Clarke y Wright.
``` 
El algoritmo se desarrolla de la siguiente manera:
1. Para n rutas: v0 → vi → v0, para cada i ≥ 1;
2. Calcule los ahorros del trafico que ingresa a las ubicaciones de entrega i y j, que viene dado por 
sij = di0 + d0j - dij, para todo i, j ≥ 1 y i 6 = j;
3. Clasifique los ahorros en orden descendente;
4. Comenzando en la parte superior de la lista (restante) de ahorros, combine las dos rutas asociadas
con los mayores ahorros (restantes), siempre que:
(a) Los dos lugares de entrega no se encuentran ya en la misma ruta;
(b) Ninguna ubicación de entrega se encuentra dentro de su misma ruta, lo que significa que ambos nodos aún están
conectados directamente al depósito en sus respectivas rutas;
(c) La demanda G y las restricciones de distancia D no son intersectadas en la ruta .
5. Repita el paso (3) hasta que no se puedan lograr ahorros adicionales.
```
