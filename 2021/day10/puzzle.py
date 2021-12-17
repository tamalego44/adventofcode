
matching = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",
    ")":"(",
    "]":"[",
    "}":"{",
    ">":"<"
}

def parseInput():
    if False:
        filename = "sample.txt"
    else:
        filename = "input.txt"

    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip())
    
    return data

def part1():
    points = {
        ")":  3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    data = parseInput()

    total = 0
    for line in data:
        stack = []
        for char in line:
            if char in points:
                if len(stack) > 0 and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    total += points[char]
                    break
            else:
                stack.append(char)

    return total

def part2():
    points = {
        ")":1,
        "]":2,
        "}":3,
        ">":4
    }

    data = parseInput()

    scores = []
    for line in data:
        stack = []
        for char in line:
            if char in points:
                if stack[-1] == matching[char]:
                    stack.pop()
                else:
                    #ignore corrupted lines
                    stack = []
                    break
            else:
                stack.append(char)

        if len(stack) > 0:
            #incomplete line
            score = 0
            for char in stack[::-1]:
                score *= 5
                score += points[matching[char]]

            scores.append(score)

    scores.sort()
    total = scores[len(scores)//2]
    return total


print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
