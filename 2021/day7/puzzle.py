from aocd import get_data # @ignore

def parseInput():
    data = get_data(day=7) # str
    data = [int(a) for a in data.split(",")]
    
    return data

def part1():
    data = parseInput()

    fuels = [None] * (max(data))
    for i in range(min(data), max(data)):
        fuel = [abs(a-i) for a in data]
        fuels[i] = sum(fuel)
    
    min_fuel = min([fuel for fuel in fuels if fuel is not None])
    return min_fuel

def part2():
    data = parseInput()

    fuels = [None] * (max(data))
    for i in range(min(data), max(data)):
        fuel = [abs(a-i) * (abs(a-i) + 1) // 2 for a in data]
        fuels[i] = sum(fuel)
    
    min_fuel = min([fuel for fuel in fuels if fuel is not None])
    return min_fuel


print("Part 1 solution:")
print(part1())

print()
print("Part 2 solution:")
print(part2())