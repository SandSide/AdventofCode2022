priorityValues = {}

def generate_priorities():
    value = 1
    for x in range(97,123):
        priorityValues[chr(x)] = value
        value +=1

    for x in range(65,91):
        priorityValues[chr(x)] = value
        value +=1

def find_double(line):

    line.strip()

    halfIndex = int(len(line)/2)

    firstSack  = line[:halfIndex]
    secondSack = line[halfIndex:len(line) -1]

    print(line)
    print(firstSack)
    print(secondSack)

    for element in firstSack:
        for n in secondSack:
            if element == n:
                return element

def find_badge(group):

    for element in group[0]:
        for x in group[1]:
            if element == x:
                # print(element)
                for y in group[2]:
                    if y == x:
                        return element

def find_badge_priority(group):


    badge = find_badge(group)

    print(group)
    print("badge {}".format(badge))
    print("priority {}\n".format(priorityValues[badge]))
    return priorityValues[badge]


def get_priority(line):
    double = find_double(line)

    priority = priorityValues[double]

    print("{} = {} \n".format(double, priority))

    return priority



def main():
    f = open('input.txt' ,'r')
    total = 0

    totalSacks = 0
    totalGroups = 0

    generate_priorities()

    group = []
    for line in f:
        totalSacks +=1
        group.append(line)

        if len(group) == 3:
            totalGroups += 1
            total += find_badge_priority(group)
            # print("{}\n".format(badge))
            group = []

    print("total sacks {} ".format(totalSacks))
    print("total groups {} ".format(totalGroups))
    print(total)
    
main()



