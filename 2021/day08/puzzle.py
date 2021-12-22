def parseInput():
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(tuple([x.strip().split(" ") for x  in line.split(" | ")]))
    return data

def part1():
    data = parseInput()
    valid = [2,3,4,7]
    
    sum = 0
    for output in [d[1] for d in data]:
        for value in output:
            if len(value) in valid:
                sum += 1

    return sum
    
def part2():
    data = parseInput()
    map = {
        2: [1],
        3: [7],
        4: [4],
        5: [2,3,5],
        6: [0,6,9],
        7: [8]
    }

    sum = 0
    
    for signals, output in data:
        map4 = {}
        map5 = {}
        for signal in signals:
            options = map[len(signal)]
            if len(options) == 1:
                map4[options[0]] = set(signal)
                map5[signal] = options[0]

        #deduce numbers
        sig = [s for s in signals if len(s) == 6 and set(s).intersection(map4[4]) == map4[4]][0]
        map5[sig] = 9
        map4[9] = set(sig)

        sig = [s for s in signals if s not in map5 and len(s) == 6 and set(s).intersection(map4[7]) == map4[7]][0]
        map5[sig] = 0
        map4[0] = set(sig)

        sig = [s for s in signals if s not in map5 and len(s) == 6][0]
        map5[sig] = 6
        map4[6] = set(sig)  

        sig = [s for s in signals if len(s) == 5 and set(s).intersection(map4[1]) == map4[1]][0]
        map5[sig] = 3
        map4[3] = set(sig)

        sig = [s for s in signals if s not in map5 and len(s) == 5 and map4[9].intersection(set(s)) == set(s)][0]
        map5[sig] = 5
        map4[5] =  set(sig)

        sig = [s for s in signals if s not in map5 and len(s) == 5][0]
        map5[sig] = 2
        map4[2] =  set(sig)

        map6 = {}
        for k,v in map5.items():
            key = "".join(sorted(k))
            map6[key] = v

        out_string = ""
        for num in output:
            out_string += str(map6["".join(sorted(num))])
        
        sum += int(out_string)

    return sum

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())