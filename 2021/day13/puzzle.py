debug = False

def parseInput():
    if debug:
        filename = "sample.txt"
    else:
        filename = "input.txt"

    data = []
    points = None
    with open(filename) as file:
        for line in file:
            if line == "\n":
                points = data
                data = []
                continue

            if points == None:
                point = tuple([int(a) for a in line.strip().split(",")])
                data.append(point)
            else:
                data.append(tuple(line.strip().split(" ")[2].split("=")))
    return points, data

def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()
    print()

def fold_board(board, fold):
    global debug

    if fold[0] == "x":
        n = int(fold[1])
        print("horizontal fold at %d" % n)
        for i in range(len(board)):
            board[i][n] = "|"
        if debug:
            print_board(board)
        
        for i in range(min(len(board[0])-n-1, n)):
            for j in range(len(board)):
                board[j][n-i-1] = board[j][n+i+1] if board[j][n-i-1] == "." else board[j][n-i-1]
        
        board = [row[0:n] for row in board]
        if debug:
            print_board(board)

    elif fold[0] == "y":
        n = int(fold[1])
        print("vertical fold at %d" % n)
        for i in range(len(board[0])):
            board[n][i] = "-"
        if debug:
            print_board(board)

        for i in range(min(len(board)-n-1, n)):
            for j in range(len(board[0])):
                board[n-i-1][j] = board[n+i+1][j] if board[n-i-1][j] == "." else board[n-i-1][j]
        
        board = board[0:n]
        if debug:
            print_board(board)
    return board

def part1():
    global debug
    
    points, instructions = parseInput()
    #print(points)
    #print(instructions)

    min_x = min([x for x,y in points])
    max_x = max([x for x,y in points])+1
    min_y = min([y for x,y in points])
    max_y = max([y for x,y in points])+1
    
    board = [['.'] * max_x for y in range(max_y)]
    
    if debug:
        print("empty:") 
        print_board(board)

    for point in points:
        #print(point)
        board[point[1]][point[0]] = "#"

    if debug:
        print_board(board)

    board = fold_board(board, instructions[0])
    #fold_board(board, instructions[0])
    
    answer = sum([1 for row in board for n in row if n == '#'])
    return answer
    
    board = fold_board(board, instructions[1])

def part2():
    points, instructions = parseInput()
    min_x = min([x for x,y in points])
    max_x = max([x for x,y in points])+1
    min_y = min([y for x,y in points])
    max_y = max([y for x,y in points])+1
    
    board = [['.'] * max_x for y in range(max_y)]
    
    if debug:
        print("empty:") 
        print_board(board)

    for point in points:
        #print(point)
        board[point[1]][point[0]] = "#"

    if debug:
        print_board(board)
    
    for instruction in instructions:
        board = fold_board(board, instruction)
    
    print_board(board)

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
