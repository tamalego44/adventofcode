sample = False
fn = "sample1.txt" if sample else "input.txt"

def parseInput(filename):
    res = []
    with open(filename) as fp:
        data = fp.readlines()
        for i, d in enumerate(data, start=1):
            rounds = d.split(":")[1].strip().split("; ")
            res.append([i, rounds])
    return res

def part1():
    maxes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    data = parseInput(fn)
    sum = 0
    for game in data:
        possible = True
        for round in game[1]:
            round = round.split(', ')
            for r in round:
                num, color = r.split(" ")
                num = int(num)
                if num > maxes[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            sum += int(game[0])

    print(sum)

def part2():
    data = parseInput(fn)
    sum = 0
    for game in data:
        maxes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in game[1]:
            round = round.split(', ')
            for r in round:
                num, color = r.split(" ")
                num = int(num)
                maxes[color] = max(maxes[color], int(num))
        
        power = maxes["red"] * maxes["green"] * maxes["blue"]
        sum += power

    print(sum)

print("Part 1:")
part1()

print("Part 2:")
part2()