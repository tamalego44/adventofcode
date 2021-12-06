def part1():
    with open("input6.txt") as file:
        for line in file:
            fish = line.strip().split(",")
            fish = [int(f) for f in fish]

    for day in range(80):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1

    print(len(fish)) 

def part2():
    fish = [0,0,0,0,0,0,0,0,0]
    with open("input6.txt") as file:
        for line in file:
            for f in line.strip().split(","):
                fish[int(f)] += 1
    
    print(fish)

    for day in range(256):
        newfish = fish[1:] + [fish[0]]
        newfish[6] += fish[0]
        fish = newfish

    print(sum(fish))

part2()