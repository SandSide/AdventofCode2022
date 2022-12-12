f = open("input.txt" ,"r")

mostCalories = [0,0,0]
currCalories = 0

totalRains = 0

print('{} \n'.format(mostCalories))

for line in f:
    if line.strip() ==  "":
        totalRains += 1

        # reverse top 3 
        mostCalories.sort(reverse=True)
      
        # check if current caloires is greater than any other 
        for index, value in enumerate(mostCalories):
            if currCalories > value:

                
                print('{} ===> {} '.format(value, currCalories))
                mostCalories[index] = currCalories

                if index == 0:
                    mostCalories[2] = value
                if index == 1:
                    mostCalories[2] = value


                # print('{} \n'.format(mostCalories))
                break

        currCalories = 0
    else:
        currCalories += int(line)

print(totalRains)

totalCal = 0
for value in mostCalories:
    totalCal += value


print(totalCal)