from collections import defaultdict
from typing import DefaultDict
import math

def parseInput():
    if False:
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

"""
function reconstruct_path(cameFrom, current)
    total_path := {current}
    while current in cameFrom.Keys:
        current := cameFrom[current]
        total_path.prepend(current)
    return total_path

// A* finds a path from start to goal.
// h is the heuristic function. h(n) estimates the cost to reach goal from node n.
function A_Star(start, goal, h)
    // The set of discovered nodes that may need to be (re-)expanded.
    // Initially, only the start node is known.
    // This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet := {start}

    // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    // to n currently known.
    cameFrom := an empty map

    // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore := map with default value of Infinity
    gScore[start] := 0

    // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    // how short a path from start to finish can be if it goes through n.
    fScore := map with default value of Infinity
    fScore[start] := h(start)

    while openSet is not empty
        // This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        current := the node in openSet having the lowest fScore[] value
        if current = goal
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        for each neighbor of current
            // d(current,neighbor) is the weight of the edge from current to neighbor
            // tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore := gScore[current] + d(current, neighbor)
            if tentative_gScore < gScore[neighbor]
                // This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] := current
                gScore[neighbor] := tentative_gScore
                fScore[neighbor] := tentative_gScore + h(neighbor)
                if neighbor not in openSet
                    openSet.add(neighbor)

    // Open set is empty but goal was never reached
    return failure
"""
dirs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
    ]

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

def astar(graph, start, goal, h):
    openSet = {start}

    cameFrom = {}

    gScore = DefaultDict(lambda: 999999)
    gScore[start] = 0

    fScore = DefaultDict(lambda: 999999)
    fScore[start] = h(start)

    while len(openSet) > 0:
        current = min(openSet, key=lambda x: fScore[x])
        #print(current)
        if current == goal:
            return reconstruct_path(cameFrom, current)
        
        openSet.remove(current)
        for dir_ in dirs: 
            neighbor = (current[0]+dir_[0],current[1]+dir_[1])
            if current[0] < 0 or current[0] >= len(graph) or current[1] < 0 or current[1] >= len(graph[0]):
                continue # neighbor out of bounds

            tentative_gScore = gScore[current] + graph[current[0]][current[1]]
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                if neighbor not in openSet:
                    openSet.add(neighbor)
    
    return -1

        
def dijkstra(G, root):
    Q = []
    dist = {}
    prev = {}
    for i in range(len(G)):
        for j in range(len(G[0])):
           v = (i,j)
           dist[v] = 99999999
           prev[v] = None
           Q.append(v)
    dist[root] = 0

    while len(Q) > 0:
        u = min(Q, key = lambda x: dist[x])
        Q.remove(u)

        for dir_ in dirs: 
            w = (u[0]+dir_[0],u[1]+dir_[1])
            if w[0] < 0 or w[0] >= len(G) or w[1] < 0 or w[1] >= len(G[0]):
                continue # neighbor out of bounds
            if w in Q:
                alt = dist[u] + G[w[0]][w[1]]
                if alt < dist[w]:
                    dist[w] = alt
                    prev[w] = u
           
    return dist, prev

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

def print_map(g):
    for row in g:
        for char in row:
            print(char, end="")
        print()

def part1():
    g = parseInput()
    
    #g = bfs(data, (0,0), (9,9))

    dist, prev = dijkstra(g, (0,0))
    
    return dist[(len(g)-1,len(g[0])-1)]

def part2():
    g = parseInput()

    #Create bigger graph
    new_graph = []
    for j in range(5):
        for row in g:
            new_graph.append([])
            for i in range(5):
                new_graph[-1] += (list(map(lambda x: ((x+i+j-1) % 9) + 1, row)))
    
    #print_map(new_graph)
    g = new_graph

    #dist, prev = dijkstra(g, (0,0))
    #return dist[(len(g)-1,len(g[0])-1)]
    end = (len(g)-1, len(g[0])-1)
    h = lambda x:  math.sqrt((end[0] - x[0])**2 + (end[1] - x[1])**2)
    ascore = sum([g[p[0]][p[1]] for p in astar(g, (0,0), end, h)]) - g[0][0]
    return ascore


print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
