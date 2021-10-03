# Algoritmo Depth-First Search (DFS)

## Pseudocódigo del algoritmo

	DFS(grafo, nodoOrigen):
		n =  tamañoGrafo
		visited = [NO_VISITADO]*n
		parent = [NULO]*n
		stack = [s]
		MIENTRAS stack no esté vacio HACER
			u = quitar_primero(stack)
			SI visited[u] = NO_VISITADO HACER
				visited[u] = VISITADO
				PARA CADA v en G[u] HACER
					SI visited[u] = NO_VISITADO HACER
						parent[v] = u
						stack.añadir(v)
		retornar parent
## Posible Análisis Asintótico

Si el grafo se representa como una lista de adyacencia:
- Cada nodo mantiene una lista de todos sus bordes adyacentes. Supongamos que hay un número V de nodos y un número E de aristas en el grafo.
- Para cada nodo, descubrimos todos sus vecinos atravesando su lista de adyacencia solo una vez en tiempo lineal.
- Para un grafo dirigido, la suma de los tamaños de las listas de adyacencia de todos los nodos es E. Entonces, la complejidad de tiempo en este caso es:
		O (V) + O (E) = O (V + E).
- El peor caso se podría dar cuando el elemento que se desea encontrar esté en las ultimas posiciones de profundidad. Esto ocasionaría un tiempo de ejecución alto.
