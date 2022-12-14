

def main():
    f = open('input.txt' ,'r')

    currMarker = ""
    markerSize = 14
    index  = 0

    temp = ""
    for x in range(1, markerSize + 1):
        temp += str(x)

    for line in f:

        print(line)
        print("\n")

        for c in line:
            currMarker += c
            index += 1
    
            if len(currMarker) == markerSize:
                print(temp)
                print(currMarker)

                valid = True
                for x in range(0,markerSize):
                    print("checking {} in {}".format(currMarker[x], currMarker[x+1:markerSize]))

                    if currMarker[x] in currMarker[x+1:markerSize]:
                        valid = False
                        break

                if valid:
                    print ("Answer {} at index {}".format(currMarker, index))
                    exit(1)

                print("\n")
                currMarker = currMarker[1:markerSize]

main()

