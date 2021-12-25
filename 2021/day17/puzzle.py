def parseInput():
    if False:
        filename = "sample.txt"
    else:
        filename = "input.txt"

    data = []
    with open(filename) as file:
        for line in file:
            line = line.split('=')
            x = line[1].split(',')[0].split('..')
            y = line[2].strip().split('..')
            data = [int(a) for a in x + y]
    
    return data

def valid(target, x, y):
    return x >= target[0] and x <= target[1] and y >= target[2] and y <= target[3]

def simulate(target, vx, vy):
    x, y = 0, 0
    maxy = 0
    while y >= target[2]: # while probe is above target area
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx <0:
            vx += 1
        vy -= 1

        maxy = max(maxy, y)

        if valid(target, x, y):
            return maxy
    return -1

def part1():
    data = parseInput()
    #print(data)

    xrange = range((data[1] - data[0]) * 3)
    yrange = range((data[3] - data[2]) * 3)

    maxy = -1
    for vx in xrange:
        for vy in yrange:
            maxy = max(maxy, simulate(data, vx, vy))

    return maxy

def part2():
    data = parseInput()

    scale = 10
    xrange = range(-(data[1] - data[0]) * scale,(data[1] - data[0]) * scale)
    yrange = range(-(data[3] - data[2]) * scale, (data[3] - data[2]) * scale)

    count = 0
    for vx in xrange:
        for vy in yrange:
            if simulate(data, vx, vy) > -1:
                count += 1

    return count

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
