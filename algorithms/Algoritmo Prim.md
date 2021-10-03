# Algoritmo de Prim

El algoritmo de Prim permite encontrar un árbol recubridor minimo, es decir un subconjunto de aristas que conforman un árbol
con todos los vértices, donde el peso total (la suma de los pesos de cada arista recorrida) es el mínimo posible.

## Pseudocodigo
``` [python]
    AlgoritmoPrim (Grafo G)
        for each u in V[G] do
            distance[u] = infinite
            parent[u] = NULL
            Add(priority,<u, distance[u]>)
        distance[u] = 0
        Update(priority,<u, distance[u]>)
        while !isEmpty(priority) do
            u = popMinimum(priority)
            for each v adjacent to 'u' do
                if ((v ∈ priority) and (distance[v] > weight(u, v)) so
                    parent[v] = u
                    distance[v] = weight(u, v)
                    Update(priority,<v, distance[v]>)
```

## Funcionamiento del algoritmo
1. Elegir un vértice cualquiera para que sea el vértice de partida.
2. Seleccionar la arista que tenga el menor peso incidente en el vértice seleccionado anteriormente y a continuación se selecciona el otro vértice en el que incide dicha arista.
3. Repetir el paso anterior siempre que la arista elegida tenga conexión con un vértice previamente seleccionado y otro que no lo esté.
5. El algoritmo finaliza cuando todos los vértices del grafo han sido seleccionados.

## Analisis asintotico del algoritmo
Usualmente la implementación del algoritmo de Prim resulta con un tiempo de complejidad O(n^2) cuando se implementa con bucles dobles. Sin embargo, en el pseudocodigo propuesto
se aprecia que la implementación es a traves de un montículo (estructura de datos del tipo árbol con información perteneciente a un conjunto ordenado), 
es decir la cola de prioridad. Debido a que el pseudocódigo se realiza de esta manera, haciendo uso de heap, se puede decir que la complejidad de este algoritmo es O(log(n)).
