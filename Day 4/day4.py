
def check_pair(pair):
    print(pair)
    pair1 = pair[0]
    pair2 = pair[0]

    pair1Range = pair[0].split("-")
    pair2Range = pair[1].split("-")

    # Check if pair 2 in pair 1
    if int(pair2Range[0]) >= int(pair1Range[0]) and int(pair2Range[1]) <= int(pair1Range[1]):
        print("Pair 2 in pair 1")
        return True

    # Check if pair 2 in pair 1
    if int(pair1Range[0]) >= int(pair2Range[0]) and int(pair1Range[1]) <= int(pair2Range[1]):
        print("Pair 1 in pair 2")
        return True
    print("\n")

    return False

def check_pair_overlap(pair):
    print(pair)

    x = pair[0].split("-")
    y = pair[1].split("-")

    for xValue in range(int(x[0]),int(x[1]) + 1):
        for yYalue in range(int(y[0]),int(y[1]) + 1):
            if xValue == yYalue:
                print(xValue)
                return True

    return False

def main():
    f = open('input.txt' ,'r')

    totalPairsInside = 0

    count = 0
    for line in f:
        line = line.strip()
        pair = line.split(",")

        if check_pair_overlap(pair):
            count +=1

    print(count)


main()