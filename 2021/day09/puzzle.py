def parseInput():

    data = []
    with open("input.txt") as file:
        for line in file:
            data.append([int(a) for a in line.strip()])
    return data

def part1():
    data = parseInput()
    risk = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if i > 0 and data[i-1][j] <= data[i][j]:
                continue
            elif i < len(data) - 1 and data[i+1][j] <= data[i][j]:
                continue
            elif j > 0 and data[i][j-1] <= data[i][j]:
                continue
            elif j < len(data[0]) - 1 and data[i][j+1] <= data[i][j]:                
                continue
            risk += 1 + data[i][j]
    
    return risk

dirs = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

def part2():
    data = parseInput()
    low_points = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if i > 0 and data[i-1][j] <= data[i][j]:
                continue
            elif i < len(data) - 1 and data[i+1][j] <= data[i][j]:
                continue
            elif j > 0 and data[i][j-1] <= data[i][j]:
                continue
            elif j < len(data[0]) - 1 and data[i][j+1] <= data[i][j]:                
                continue
            low_points.append((i, j))
    
    basins = []
    for low_point in low_points:
        basin = []
        queue = [low_point]
        #invalid = []
        #print("===", low_point, "===")
        # print(len(data[0]))
        # print(range(max(0,p[0]-1), min(len(data), p[0]+1)))
        # print(range(max(0,p[1]-1), min(len(data[0]), p[1]+1)))
        
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr not in basin and data[curr[0]][curr[1]] < 9:
                basin.append(curr)
                for dir_ in dirs:
                    new = (curr[0] + dir_[0], curr[1]+dir_[1])
                    if new[0] < 0 or new[0] >= len(data) or new[1] < 0 or new[1] >= len(data[0]):
                        continue # Out of bounds

                    if new not in basin:
                        queue.append(new)
        
        #print(basin)
        basins.append(len(basin))
    
    basins.sort()
    score = basins[-3] * basins[-2] * basins[-1]
    return score


print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())