import sys

def parseInput():
    if True:
        filename = "sample.txt"
    else:
        filename = "input.txt"

    data = []
    with open(filename) as file:
        for line in file:
            data.append([])
            for n in line.strip():
                data[-1].append(int(n))
    
    return data

"""
 1  procedure BFS(G, root) is
2      let Q be a queue
3      label root as explored
4      Q.enqueue(root)
5      while Q is not empty do
6          v := Q.dequeue()
7          if v is the goal then
8              return v
9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as explored then
11                  label w as explore
12                  Q.enqueue(w)
"""

"""
1  function Dijkstra(Graph, source):
2
3      create vertex set Q
4
5      for each vertex v in Graph:            
6          dist[v] ← INFINITY                 
7          prev[v] ← UNDEFINED                
8          add v to Q                     
9      dist[source] ← 0                       
10     
11      while Q is not empty:
12          u ← vertex in Q with min dist[u]   
13                                             
14          remove u from Q
15         
16          for each neighbor v of u still in Q:
17              alt ← dist[u] + length(u, v)
18              if alt < dist[v]:              
19                  dist[v] ← alt
20                  prev[v] ← u
21
22      return dist[], prev[]
"""
dirs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
    ]
        
def dijkstra(G, root):
    Q = []
    dist = {}
    prev = {}
    for i in range(len(G)):
        for j in range(len(G[0])):
           v = (i,j)
           dist[v] = sys.maxint
           prev[v] = None
           Q.append(v)
    dist[root] = 0

    while len(Q) > 0:
        u = min([dist[u] for u in Q])
        
        Q.remove(u)

        for dir_ in dirs: 
            w = (v[0]+dir_[0],v[1]+dir_[1])
            if w[0] < 0 or w[0] >= len(G) or w[1] < 0 or w[1] >= len(G[0]):
                continue # neighbor out of bounds
            if w not in explored:
                explored.append(w)
                queue.append(w)
            

def bfs(G, root, goal):
    queue = []
    explored = [root]
    queue.append(root)

    while len(queue) > 0:
        v = queue.pop(0)
        if v == goal:
            print(explored)
            print(queue)
            return v #TODO
        
        for dir_ in dirs:
            w = (v[0]+dir_[0],v[1]+dir_[1])
            if w[0] < 0 or w[0] >= len(G) or w[1] < 0 or w[1] >= len(G[0]):
                continue # neighbor out of bounds
            if w not in explored:
                explored.append(w)
                queue.append(w)


def part1():
    data = parseInput()
    g = bfs(data, (0,0), (9,9))
    print(g)

def part2():
    data = parseInput()

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
