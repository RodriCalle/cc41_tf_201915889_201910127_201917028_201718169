# **Algoritmo Breadth First Search (BFS)**

## Pseudocódigo

``` [python]
      BFS (G, nInicio)        //Donde G es el grafo y nInicio es el nodo de origen
          permitir a C ser la cola
          C.queue( nInicio )        //Insertar nInicio en cola hasta que todos sus vértices vecinos estén marcados
          marcar nInicio como visitado
          while ( C no está vacío )
              //Eliminando ese vértice de la cola, cuyo vecino será visitado ahora
              V  =  C.queue( )
              //Procesando todos los vecinos de v  
              for todos los vecinos i de V in el grafo G
                  if i not in visitado
                            C.queue( i )        //Almacena i en C para visitar a sus vecinos
                            marcar i como visitado
```

## Posible análisis asintótico

- La complejidad temporal de BFS si se atraviesa todo el árbol e
