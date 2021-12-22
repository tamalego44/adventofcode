
def winning(mask):
    #Horizontal Win
    for mline in mask:
        if 0 not in mline:
            return True
    
    #Vertical Win
    for i in range(5):
        mline = [line[i] for line in mask]
        if 0 not in mline:
            return True
    
    # #Diagonal Win
    # mline = [mask[i][i] for i in range(5)]
    # if 0 not in mline:
    #     return True

    # mline = [mask[i][4-i] for i in range(5)]
    # if 0 not in mline:
    #     return True

    return False

def calc_score(board, mask, num):
    sum = 0
    for bline, mline in zip(board, mask):
        for bcol, mcol in zip(bline, mline):
            if mcol == 0:
                sum += bcol
    
    return sum * num

def createdata():
    i = 0
    currBoard = None
    boards = []
    currMask = []
    masks = []
    with open("input4.txt") as file:
        for line in file:
            if i == 0:
                order = [int(a) for a in line.split(",")]
            elif currBoard == None:
                currBoard = []
            else:
                currBoard.append([int(a) for a in line.split()])
                currMask.append([0 for a in line.split()])
                if i % 6 == 0:
                    boards.append(currBoard)
                    masks.append(currMask)
                    currBoard = None
                    currMask = []
            i += 1

    return order, boards, masks
    
def part1():
    order, boards, masks = createdata()

    # game loop
    for num in order:
        print("Calling: %d" % num)
        #check every board for num
        for boardnum in range(len(boards)):
            for linenum in range(len(boards[boardnum])):
                for colnum in range(len(boards[boardnum][linenum])):
                    if boards[boardnum][linenum][colnum] == num:
                        masks[boardnum][linenum][colnum] = 1
        
        #check if any boards are winning
        for board, mask in zip(boards, masks):
            if winning(mask):
                score = calc_score(board, mask, num)
                print(score)
                return score

def part2():
    order, boards, masks = createdata()
    
    # game loop
    remaining = len(boards)
    for num in order:
        print("Calling: %d" % num)
        #check every board for num
        for boardnum in range(len(boards)):
            for linenum in range(len(boards[boardnum])):
                for colnum in range(len(boards[boardnum][linenum])):
                    if boards[boardnum][linenum][colnum] == num:
                        masks[boardnum][linenum][colnum] = 1
        
        #check if any boards are winning
        for board, mask in zip(boards, masks):
            if winning(mask):
                if remaining == 2:
                    print(boards)
                    print(masks)
                
                if remaining == 1:
                    print(boards)
                    print(masks)
                    score = calc_score(board, mask, num)
                    print(score)
                    return(score)
                else:
                    remaining -= 1
                    boards.remove(board)
                    masks.remove(mask)



part2()