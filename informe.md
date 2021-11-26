# Problema de Enrutamiento(VRP)
#### CC41 - TRABAJO FINAL COMPLEJIDAD ALGORÍTMICA 2021

INTEGRANTES | CODIGO| 
-|-|
Carlos Leon Rupay| u201917028  
Adrian Esqueiros Cabrera|u201718169 | 
Rodrigo Calle Galdos|u201915889|
Juan de Dios Quiroz Rodríguez|u201910127|

##  INTRODUC
Este trabajo consiste en resolver el problema de enrutamiento de vehículos, más conocido como VRP, en su versión para múltiples puntos de distribución. A menudo, este suele ser un problema bastante común en las empresas de reparto de bienes y productos, pues lo que ellos buscan es encontrar la ruta de entrega más óptima tomando en cuenta diversos factores tales como el lugar de sus almacenes, la distancia entre sus almacenes hacia los diferentes puntos de entrega, así como también ciertos recursos como los vehículos a usar, el combustible, tiempo, etc.
 
## MARCO TEÓRICO
### Algoritmo DFS (Breadth First Search)
El algoritmo de búsqueda en profundidad es utilizado para recorrer todos los nodos de un grafo de manera ordenada, pero no uniforme. Su funcionamiento consiste en ir expandiendo todos y cada uno de los nodos que va localizando, de forma recurrente, en un camino concreto
> -   El algoritmo DFS emplea la tecnica de Backtracking para resolver los problemas.

### Algoritmo de Prim
El algoritmo de Prim permite encontrar un árbol recubridor minimo, es decir un subconjunto de aristas que conforman un árbol con todos los vértices, donde el peso total (la suma de los pesos de cada arista recorrida) es el mínimo posible.
> -El algoritmo prim posee una complejidad de O (n ^ 2) en donde es posible realizarlo más eficientemente llegando a tener una complejidad de O (nlogn).

### Algoritmo BFS (Breadth First Search)
Este algoritmo examina todos los nodos de un árbol sistemáticamente para buscar el camino más corto partiendo de un punto específico.
> -   La complejidad del algoritmo BFS está representado por O(V + E).

### Algoritmo DYC (Divide and Conquer)
Como sugiere el nombre, es descomponer un gran problema en varios subproblemas, y luego resolvemos estos subproblemas uno por uno. Una vez resueltos todos los subproblemas, el gran problema general está resuelto.
> - Es la base de los algoritmos eficientes para casi cualquier tipo de problema como, por ejemplo, algoritmos de ordenamiento (quicksort, mergesort, entre muchos otros),


# DESARROLLO
## Generacion del Dataset
Algoritmo mediante el cual se generan de manera aleatoria los arreglos de los puntos de almacen y los puntos de entrega.

1.  Primero se genera la cantidad de almacenes entre 50 y 100, y la cantidad de entregas entre 2500 y 5000.
2.  Luego creamos los arreglos de almacenes y entregas vacíos.
3.  Posteriormente se genera dos arreglos "x" e "y" para almacen y otros dos para entrega, el rango de valor que puede tomar el "x" o "y" esta entre 1 y 1000
4.  Para finalizar se recorre los arreglos principales (almacenes y entregas) y se añaden los pares ordenados.
<pre>
qAlm = random.randint(50,100)
qEnt = random.randint(2500,5000)

almacenes, entregas = [], []

almacenx = np.random.randint(1,1000, size=qAlm)
almaceny = np.random.randint(1,1000, size=qAlm)

entregax = np.random.randint(1,1000, size=qEnt)
entregay = np.random.randint(1,1000, size=qEnt)

for i in range(qAlm):
  almacenes.append( [almacenx[i], almaceny[i]] )
for i in range(qEnt):
  entregas.append( [entregax[i], entregay[i]] )

Una vez generado los arreglos con los pares ordenados para cada punto, se escriben en arcchivos. El arreglo almacenes se escribe en el archivo "puntos_almacenes.csv" y el arreglo entregas en "puntos_entregas.csv"

almacenesFile = open('puntos_almacenes.csv', 'w')
with almacenesFile:
  writer = csv.writer(almacenesFile)
  writer.writerows(almacenes)

entregasFile = open('puntos_entrega.csv', 'w')
with entregasFile:
  writer = csv.writer(entregasFile)
  writer.writerows(entregas)
</pre>

## Creación del Grafo
Se importa las librerías y la información de los dataset de los puntos de entrega y los almacenes, ambos en archivos  **CSV**  que se usara para la creación del grafo.
<pre>
def setEmptyGraph(size):
  n = size*size
  G = [ [] for _ in range(n) ]
  for x in range(size):
    for y in range(size):
      if(size > x + 1):
        G[ ((x * size) + y) ].append(((x+1) * size) + y)
      if(0 <= x - 1):
        G[ ((x * size) + y) ].append(((x-1) * size) + y)
      if(size > y + 1):
        G[ ((x * size) + y) ].append((x * size) + (y+1))
      if(0 <= y - 1):
        G[ ((x * size) + y) ].append((x * size) + (y-1))
  return G

def setKnownPoints(size, almacen, entrega):
  id = ["empty"]*(size*size)
  for a in almacen:
    x, y = a[0], a[1]
    pos = x*size + y
    id[pos] = "A"
  for a in entrega:
    x, y = a[0], a[1]
    pos = x*size + y
    id[pos] = "E"
  return id

def getGraphWeighted(G):
  adjlListWeighted = [[] for i in range(len(G))]
  for i in range(len(G)):
    for j in range(len(G[i])):
      adjlListWeighted[i].append(   ( G[i][j], round( math.sqrt( (( (i // (len(G)/2) ) - (G[i][j] //  (len(G)/2) ) )**2) + (( (i %  (len(G)/2) ) - (G[i][j] %  (len(G)/2) ) )**2)   )          )  )    )
  return adjlListWeighted
</pre>
 
## Algoritmo de Dijkstra de cada almacen a los puntos de entrega
Se utiliza el algoritmo de dijkstra a cada almacen para dividirlo a cada uno de los puntos de entrega generados en el dataset.
  <pre>
def getAlmPoint(size, almacen):
  alm = []
  for a in almacen:
    x, y = a[0], a[1]
    pos = x*size + y
    alm.append(pos)
  return alm

def getCoord(pos, size):
  x = pos // size
  y = pos % size
  return [x, y]

def getEntPoint(size, entrega):
  ent = []
  for a in entrega:
    x, y = a[0], a[1]
    pos = x*size + y
    ent.append(pos)
  return ent

def dijkstraEntregas(almacenes, entregas, G):
  sol = [] 
  for i in almacenes:
    path, cost = dijkstra(G,i)
    for j in entregas:
      node = j
      p = [j]
      c = cost[j]
      while node != i:
        node = path[node]
        p.append(node)
      p.reverse()
      sol.append((i,j,c,p))
  return sol
</pre>
## Algoritmo para repartir puntos de entrega entre almacenes, utilizar criterio de cercanía.
Ahora se desarrollo un nuevo algoritmo que nos permita repartir los puntos de entrega pero utilizando el criterio de cercania para su almacen más cercano.
<pre>
groupsAlm = [[] for _ in range(4)]
groupsEnt = [[] for _ in range(4)]
size = 4

for i in range(len(alm)):
  if ( alm[i][0]  >= 0 and alm[i][0] <= (size/2)-1 and alm[i][1] >= 0 and alm[i][1] <= (size/2)-1 ):
    groupsAlm[0].append( alm[i] )
  if ( alm[i][0] >= 0 and alm[i][0] <= (size/2)-1 and alm[i][1] >= size/2 and alm[i][1] <= size-1 ):
    groupsAlm[1].append( alm[i] )
  if ( alm[i][0] >= size/2 and alm[i][0] <= size-1 and alm[i][1] >= 0 and alm[i][1] <= (size/2)-1 ):
    groupsAlm[2].append( alm[i] )
  if ( alm[i][0] >= size/2 and  alm[i][0] <= size-1 and alm[i][1] >= size/2 and alm[i][1] <= size-1 ):
    groupsAlm[3].append( alm[i] )

for i in range(len(ent)):
  if ( ent[i][0]  >= 0 and ent[i][0] <= (size/2)-1 and ent[i][1] >= 0 and ent[i][1] <= (size/2)-1 ):
    groupsEnt[0].append( ent[i] )
  if ( ent[i][0] >= 0 and ent[i][0] <= (size/2)-1 and ent[i][1] >= size/2 and ent[i][1] <= size-1 ):
    groupsEnt[1].append( ent[i] )
  if ( ent[i][0] >= size/2 and ent[i][0] <= size-1 and ent[i][1] >= 0 and ent[i][1] <= (size/2)-1 ):
    groupsEnt[2].append( ent[i] )
  if ( ent[i][0] >= size/2 and  ent[i][0] <= size-1 and ent[i][1] >= size/2 and ent[i][1] <= size-1 ):
    groupsEnt[3].append( ent[i] )

print(groupsAlm)
print(groupsEnt)
</pre>
# SOLUCIONES

Para encontrar la solución más optima para el Problema de Enrutamiento de Vehículos (VRP) se implementaron 4 algoritmos (1 por integrante).
### ALGORITMO 1 - PRIM
<pre>

</pre>
### ALGORITMO 2 - Divide and Conquer
<pre>

</pre>
### ALGORITMO 3 - DFS
<pre>

</pre>
### ALGORITMO 4 - BFS
<pre>

</pre>
## CONCLUSIONES

-   La principal diferencia entre el TSP y el VRP consiste en la consideración de varios vehículos en el modelo de enrutamiento 
-   Tanto los algoritmos BFS,DYC, DFS y PRIM no elegidos ideales, ya que no presentan el rendimiento suficiente para soportar el presente 
-  Terminamos considerando que el algoritmo Djikstra es el más adecuado para la solucion del problema de enrutamiento solicitado
- Gracias al trabajo realizado pudimos ahondarnos mucho más en el lenguaje de programacion Phyton ,el cual hasta el principio del semestre era nuevo para nosotros
-  Finalmente el uso de herramientas como Github nos permitio conocer más acerca del uso de Issues y commit, lo cual nos ayudara muchisimo en futuros proyectos

## BIBLIOGRAFÍA

-   Robinson, S. (2021, 21 noviembre). Graphs in Python: Dijkstra’s Algorithm. Stack Abuse.  [https://stackabuse.com/dijkstras-algorithm-in-python/](https://stackabuse.com/dijkstras-algorithm-in-python/)
-  Kripkit (2021). _Búsqueda de Profundidad Limitada_ . Recuperado de: [https://kripkit.com/bsqueda-de-profundidad-limitada/](https://kripkit.com/bsqueda-de-profundidad-limitada/)
-  Estructura de Datos II (2016). _Algoritmo de Prim_ . Recuperado de: [https://estructurasite.wordpress.com/algoritmo-de-prim/](https://estructurasite.wordpress.com/algoritmo-de-prim/)
- Janas.Wordpress (2012). _ALGORITMO DE BÚSQUEDA: DEPTH FIRST SEARCH _ . Recuperado de: 
[https://jariasf.wordpress.com/2012/03/02/algoritmo-de-busqueda-depth-first-search-parte-1/](https://jariasf.wordpress.com/2012/03/02/algoritmo-de-busqueda-depth-first-search-parte-1/)
