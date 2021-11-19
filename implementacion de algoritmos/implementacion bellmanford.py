def bellmanFord(G, s):
  n = len(G)
  cost = [float('inf')]*n
  cost[s]=0
  path = [-1]*n

  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        if cost[u] + w < cost[v]:
          cost[v] = cost[u]+w
          path[v]=u
  
  for u in range(n):
    for v, w in G[u]:
      if cost[u]+w<cost[v]:
        return None, None

  return path, cost
