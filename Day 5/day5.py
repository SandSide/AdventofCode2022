
from array import *

def find_crates(line):
    temp = 0
    crate = ""

    newPile = []

    # Find crates
    for c in line:
        index = 0
        temp += 1
        crate += c

        if temp == 4:
            if "[" in crate:
                newPile.append(crate[1])
            else:
                newPile.append("#")
            
            crate = ""
            temp = 0


    return newPile  


def convert_to_stacks(piles):

    index = 0

    stackList = []

    for x in range(1,len(piles[0]) + 1):
        stackList.append([])

    for pile in piles[::-1]:
        for crate in pile:
            if crate != "#":
                stackList[index].append(crate)

            index += 1

        index = 0
        
    return stackList

def peform_instruction(instruction, stacks):

    instruction = instruction.strip()
    temp = instruction.split(" ")

    moveNum = int(temp[1])
    fromMove = int(temp[3]) - 1
    toMove = int(temp[5]) - 1
    
    multipleCrates = []

    print("moving {} from {}".format(moveNum, stacks[fromMove][::-1]))

    stackPrev = stacks[toMove][::-1]
    for x in range(0, moveNum):
        
        if len(stacks[fromMove]) > 0:
            crate = stacks[fromMove].pop()
            multipleCrates.append(crate)

    

    print(multipleCrates)

    for crate in multipleCrates[::-1]:
        stacks[toMove].append(crate)

    print("prev {}".format(stackPrev))
    print("now {}".format(stacks[toMove][::-1]))

    print("\n")
    return stacks

def get_top_of_stacks(stacks):

    top = ""
    for stack in stacks:
        top += stack.pop()

    return top


def main():
    f = open('input.txt' ,'r')
    tempPiles = []
    stacks = []

    steps = 0

    for line in f:

        # if(steps == 4):
        #     break

        # If a crate
        if "[" in line:
            tempPiles.append(find_crates(line))

        # If space before instructions
        if len(line) == 1:
            stacks = convert_to_stacks(tempPiles)
 
        if "move" in line:
            peform_instruction(line, stacks)


    top = get_top_of_stacks(stacks)
        
    print(top)


main()