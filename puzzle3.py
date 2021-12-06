

def part1():
    count_zeroes = []
    count_ones = []
    for i in range(12):
        count_zeroes.append(0)
        count_ones.append(0)
    with open("input3.txt") as file:
        for line in file:
            i = 0
            #print("\"%s\"" % line)
            for char in line:
                if char == '1':
                    count_ones[i] += 1
                elif char == '0':
                    count_zeroes[i] += 1
                i += 1

    gamma = 0
    epsilon = 0
    scale = 1
    for zero, one in zip(count_zeroes[::-1], count_ones[::-1]):
        if one > zero:
            gamma += scale
        else:
            epsilon += scale
        scale *= 2

    # gamma = ""
    # epsilon = ""
    # for zero, one in zip(count_zeroes, count_ones):
    #     if one > zero:
    #         gamma += "1"
    #         epsilon += "0"
    #     else:
    #         epsilon += "1"
    #         gamma += "0"


    print(gamma)
    print(epsilon)
    print(epsilon * gamma)

def part2():
    numbers = []
    with open("input3.txt") as file:
        for line in file:
            numbers.append(line.strip())

    numbers_copy = numbers
    z, o = 0, 0
    for i in range(len(numbers[0])):
        for num in numbers:
            if num[i] == '0':
                z += 1
            else:
                o += 1

        if z > o:
            numbers = [num for num in numbers if num[i] == '0']
        else:
            numbers = [num for num in numbers if num[i] == '1']

        z, o = 0, 0
        if len(numbers) == 1:
            num1 = int(numbers[0], 2)
    
    numbers = numbers_copy
    for i in range(len(numbers[0])):
        for num in numbers:
            if num[i] == '0':
                z += 1
            else:
                o += 1

        if z > o:
            numbers = [num for num in numbers if num[i] == '1']
        else:
            numbers = [num for num in numbers if num[i] == '0']

        z, o = 0, 0
        if len(numbers) == 1:
            num2 = int(numbers[0], 2)

    print(num1)
    print(num2)
    print(num1 * num2)
part2()