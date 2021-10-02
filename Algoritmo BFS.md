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

- La complejidad temporal de BFS si se atraviesa todo el árbol es O (V) donde V es el número de nodos.
- Si el gráfico se representa como una lista de adyacencia:
  - Cada nodo mantiene una lista de todos sus bordes adyacentes. Supongamos que hay un número V de nodos y un número E de aristas en el gráfico.
  - Para cada nodo, descubrimos todos sus vecinos atravesando su lista de adyacencia solo una vez en tiempo lineal.
  - Para un gráfico dirigido, la suma de los tamaños de las listas de adyacencia de todos los nodos es E. Entonces, la complejidad de tiempo en este caso es O (V) + O (E) = O (V + E). 
  - Para un gráfico no dirigido, cada borde aparece dos veces. Una vez en la lista de adyacencia de cualquier extremo del borde. La complejidad de tiempo para este caso será O (V) + O (2E) ~ O (V + E).
- Si el gráfico se representa como una matriz de adyacencia (una matriz V x V):
  - Para cada nodo, tendremos que recorrer una fila completa de longitud V en la matriz para descubrir todos sus bordes salientes.
  - Tener en cuenta que cada fila en una matriz de adyacencia corresponde a un nodo en el gráfico, y esa fila almacena información sobre los bordes que emergen del nodo. Por tanto, la complejidad temporal de BFS en este caso es O (V * V) = O (V^2). 
- La complejidad temporal de BFS depende en realidad de la estructura de datos que se utilice para representar el gráfico.
