file = open("/workspaces/AoC_2023/day3/part1/list.txt", "r")

numberList = []
linesList = []

realNumber = ""
for lines in file:
    linesList.append(lines)

                 
for cases in linesList:
    #i = 0
    for keys in cases:
        #print(keys)
        if keys.isdigit():
            realNumber = realNumber + keys
        else:
            if realNumber != "":
                numberList.append(realNumber)
                realNumber = ""
    
print(numberList)



    