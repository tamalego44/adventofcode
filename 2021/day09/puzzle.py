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


def part2():
    data = parseInput()

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())