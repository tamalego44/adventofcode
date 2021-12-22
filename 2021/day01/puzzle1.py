def part1():
    i = 0
    j = 0
    with open("input1.txt") as file:
        for line in file:
            if int(line) > i:
                j += 1
                i = int(line)
    
    print(j)


def part2():
    ints = []

    with open("input1.txt") as file:
        for line in file:
            ints.append(int(line))

    prev_sum = ints[0] + ints[1] + ints[2]
    j = 0
    for i in range(len(ints) - 2):
        sum = ints[i] + ints[i+1] + ints[i+2]
        if sum > prev_sum:
            j += 1
        prev_sum = sum
    print(j)

part2()