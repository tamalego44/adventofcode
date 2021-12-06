
def createdata():
    lines = []
    with open("input5.txt") as file:
        for line in file:
            points = line.strip().split(" -> ")
            line = []
            for a in points:
                a = a.split(",")
                a = [int(b) for b in a]
                line += a
            lines.append(line)
    
    return lines

def creategrid():
    size = 1000 #?
    return [[0 for j in range(size)] for i in range(size)]

def straightlines(grid, slines):
    for line in slines:
        x1 = line[0]
        x2 = line[2]
        y1 = line[1]
        y2 = line[3]
        xsign = 1 if x2 >= x1 else -1
        ysign = 1 if y2 >= y1 else -1
        #print(xsign, ysign)
        #print(line)
        for x in range(x1, x2 + xsign, xsign):
            for y in range(y1, y2 + ysign, ysign):
                grid[x][y] += 1
    
    return grid

def diagonallines(grid, dlines):
    for line in dlines:
        x1 = line[0]
        x2 = line[2]
        y1 = line[1]
        y2 = line[3]

        dx = x2 - x1
        dy = y2 - y1

        count = abs(dx)

        signx = int(dx / abs(dx))
        signy = int(dy / abs(dy))

        for i in range(count + 1):
            x = x1 + (i * signx)
            y = y1 + (i * signy)

            grid[x][y] += 1
    
    return grid

def part1():
    lines = createdata()
    grid = creategrid()

    #filter straight lines
    slines = [line for line in lines if line[0] == line[2] or line[1] == line[3]]
    
    grid = straightlines(grid, slines)

    filtered_grid = [[1 if cell > 1 else 0 for cell in line] for line in grid]
    summed_grid = sum([sum(line) for line in filtered_grid])
    print(summed_grid)

def part2():
    lines = createdata()
    grid = creategrid()

    #filter straight lines
    slines = [line for line in lines if line[0] == line[2] or line[1] == line[3]]

    grid = straightlines(grid, slines)

    dlines = [line for line in lines if line not in slines]
    
    grid = diagonallines(grid, dlines)
        
    filtered_grid = [[1 if cell > 1 else 0 for cell in line] for line in grid]
    summed_grid = sum([sum(line) for line in filtered_grid])
    print(summed_grid)
        

part2()