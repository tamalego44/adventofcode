def part1():
    h = 0
    d = 0
    with open("input2.txt") as file:
        for line in file:
            command, value = line.split(" ")
            value = int(value)

            if command == "forward":
                h += value
            elif command == "up":
                d -= value
            elif command == "down":
                d += value
            
    print(h * d)

def part2():
    h = 0
    d = 0
    aim = 0

    with open("input2.txt") as file:
        for line in file:
            command, value = line.split(" ")
            value = int(value)

            if command == "forward":
                h += value
                d += aim * value
            elif command == "up":
                aim -= value
            elif command == "down":
                aim += value
            
    print(h * d)

part2()