sample = False
fn = "sample2.txt" if sample else "input.txt"

def parseInput(filename):
    with open(filename) as fp:
        lines = fp.readlines()
    return lines

def part1():
    data = parseInput(fn)
    data = [[c for c in datum if c.isdigit()] for datum in data]
    nums = [int(datum[0] + datum[-1]) for datum in data]
    print(sum(nums))

def part2():
    data = parseInput(fn)
    repl = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    vals = []
    for i in range(len(data)):
        vals.append([])
        # start from front
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                vals[i].append(data[i][j])
            else:
                for k,v in repl.items():
                    if data[i][j:].startswith(k):
                        vals[i].append(str(v))
            if len(vals[i]) > 0:
                break

        for j in range(len(data[i]))[::-1]:
            if data[i][j].isdigit():
                vals[i].append(data[i][j])
            else:
                for k,v in repl.items():
                    if data[i][j:].startswith(k):
                        vals[i].append(str(v))
            if len(vals[i]) > 1:
                break

    nums = [int(datum[0] + datum[-1]) for datum in vals]
    # print(nums)
    print(sum(nums))

print("Part 1:")
part1()

print("Part 2:")
part2()