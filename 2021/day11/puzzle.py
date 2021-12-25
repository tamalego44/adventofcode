
def parseInput():
    data = []

    if False:
        filename = "sample.txt"
    else:
        filename = "input.txt"

    with open(filename) as file:
        for line in file:
            data.append([])
            for char in line.strip():
                data[-1].append(int(char))
    
    return data

def flash(data, i0, j0):
    for i in range(max(0,i0-1), min(len(data), i0+2)): 
        for j in range(max(0,j0-1), min(len(data[0]), j0+2)):
            if not (i == i0 and j == j0) and data[i][j] != -1:
                #print((i, j))
                data[i][j] += 1
    return data

def part1():
    data = parseInput()

    flashes = 0
    for step in range(100):
        done = False
        #Updating
        for i in range(len(data)):
                for j in range(len(data)):
                    data[i][j] += 1
        
        #Flashing
        while not done:
            done = True
            for i in range(len(data)):
                for j in range(len(data)):
                    if data[i][j] > 9:
                        #print((i,j), "===")
                        flashes += 1
                        data[i][j] = -1
                        data = flash(data, i, j)
                        done = False
                        #exit()
        
        #restore 
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j] == -1:
                    data[i][j] = 0
        
    print(data)
    return flashes

def part2():
    data = parseInput()

    step = 0
    while True:
        step += 1
        done = False
        #Updating
        for i in range(len(data)):
                for j in range(len(data)):
                    data[i][j] += 1
        
        #Flashing
        while not done:
            done = True
            for i in range(len(data)):
                for j in range(len(data)):
                    if data[i][j] > 9:
                        #print((i,j), "===")
                        data[i][j] = -1
                        data = flash(data, i, j)
                        done = False
                        #exit()
        
        #restore 
        simultaneous = True
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j] == -1:
                    data[i][j] = 0
                else:
                    simultaneous = False
        
        if simultaneous:
            return step
        

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
