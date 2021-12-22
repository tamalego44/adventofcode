def parseInput():
    if False:
        filename = "sample.txt"
    else:
        filename = "input.txt"

    data = {}
    polymer = None
    with open(filename) as file:
        for line in file:
            if polymer is None:
                polymer = line.strip()
            elif line == "\n":
                continue
            else:
                rule = line.strip().split(" -> ")
                data[rule[0]] = rule[1]
    
    return polymer, data

def part1():
    polymer, rules = parseInput()
    #print(polymer)
    #print(rules)

    for step in range(10):
        pairs = []
        for i in range(len(polymer)-1):
            pairs.append(polymer[i:i+2])
        
        new = [None] * len(pairs)
        
        newpolymer = ""
        for i in range(len(pairs)):
            newpolymer += pairs[i][0]
            if pairs[i] in rules:
                newpolymer += rules[pairs[i]]
                new[i] = rules[pairs[i]]
        newpolymer += polymer[-1]

        #print(pairs)
        #print(new)
        #print(newpolymer)
        polymer = newpolymer

    counts = {}
    for c in polymer:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1

    max_val = max(counts.values())
    min_val = min(counts.values())

    return max_val - min_val

def dict_inc(d, k, v=1):
    if k not in d:
        d[k] = v
    else:
        d[k] += v

def part2():
    polymer, rules = parseInput()
    
    pairs = {}
    for i in range(len(polymer)-1):
        dict_inc(pairs, polymer[i:i+2])
        
    for step in range(40):
        new_pairs = {}
        for pair, count in pairs.items():
            if pair in rules:
                dict_inc(new_pairs, pair[0] + rules[pair], count)
                dict_inc(new_pairs, rules[pair] + pair[1], count)
            else:
                dict_inc(new_pairs, pair, count)

        pairs = new_pairs
        #print(pairs)

    counts = {}
    for pair, count in pairs.items():
        dict_inc(counts, pair[0], count)
        dict_inc(counts, pair[1], count)
    
    counts[polymer[0]] += 1
    counts[polymer[-1]] += 1
    
    for k,v in counts.items():
        counts[k] = v//2
    
    #print(counts)

    max_val = max(counts.values())
    min_val = min(counts.values())
    
    return max_val - min_val

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
