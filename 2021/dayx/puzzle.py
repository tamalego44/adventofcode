def parseInput():
    if True:
        filename = "sample.txt"
    else:
        filename = "input.txt"

    data = []
    with open(filename) as file:
        for line in file:
            data.append(line)
    
    return data

def part1():
    data = parseInput()

def part2():
    data = parseInput()

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
