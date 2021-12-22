from aocd import get_data

def parseInput():
    data = get_data(day=7) # str
    data = [int(a) for a in data.split(",")]
    return data

def part1():
    data = parseInput()
    return min([sum([abs(a-i) for a in data]) for i in range(min(data), max(data))])

def part2():
    data = parseInput()
    return min([sum([abs(a-i) * (abs(a-i) + 1) // 2 for a in data]) for i in range(min(data), max(data))])


print("Part 1 solution:")
print(part1())

print()
print("Part 2 solution:")
print(part2())