def parseInput():
    if False:
        filename = "sample2.txt"
    else:
        filename = "input.txt"
    
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip().split('-'))
    
    return data

class Graph():

    def __init__(self, edges):
        self.graph = {}
        self.paths = []

        for e in edges:
            self.addEdge(e)

    def addEdge(self, e):
        if e[0] not in self.graph:
            self.graph[e[0]] = []
        if e[1] not in self.graph:
            self.graph[e[1]] = []
        
        if e[1] not in self.graph[e[0]]:
            self.graph[e[0]].append(e[1])
        if e[0] not in self.graph[e[1]]:
            self.graph[e[1]].append(e[0])

    def findAllPaths(self, start='start', end='end', visited={}, path=[]):
        #Base case
        path.append(start)
        visited[start] = True
        if start == end:
            self.paths.append(path.copy())
        else:
            for e in self.graph[start]:
                if e.isupper() or not visited.get(e, False):
                    self.findAllPaths(start=e, end=end, visited=visited, path=path)
        
        path.pop()
        visited[start] = False

    def findAllPaths2(self, start='start', end='end', visited={}, flag=False, path=[]):
        #print(start, end, visited, flag, path)
        #Base case
        path.append(start)
        visited[start] = True
        if start == end:
            self.paths.append(path.copy())
        else:
            for e in self.graph[start]:
                if flag or e in ['start', 'end']:
                    if e.isupper() or not visited.get(e, False):
                        self.findAllPaths2(start=e, end=end, visited=visited, flag=flag, path=path)
                else:
                    if e.islower() and visited.get(e, False):
                        self.findAllPaths2(start=e, end=end, visited=visited, flag=e, path=path)
                    else:
                        self.findAllPaths2(start=e, end=end, visited=visited, flag=flag, path=path)
        
        path.pop()
        if flag != start:
            visited[start] = False

def part1():
    data = parseInput()

    #print(data)

    graph = Graph(data)
    #print(graph.graph)
    graph.findAllPaths()
    #print(graph.paths)

    return len(graph.paths)

def part2():
    data = parseInput()
    
    graph = Graph(data)
    graph.findAllPaths2()
    return len(graph.paths)

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())