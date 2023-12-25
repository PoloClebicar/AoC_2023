import queue

def main():
    #Set up the Queue 
    fileQ = queue.Queue()

    file = open("/workspaces/AoC_2023/day5/part1/list.txt", "r")

    for lines in file:
        fileQ.put(lines)

    seedList = createSeedList(fileQ)
    #print("Seed List: ", seedList)

    #seed-to-soil map:
    seedRawCoord = generateCoordinates(fileQ)
    mapList = treatCoordinates(seedRawCoord)
    newSeedList = compareList(seedList, mapList)

    for _ in range(6):
        seedRawCoord = generateCoordinates(fileQ)
        mapList = treatCoordinates(seedRawCoord)
        newSeedList = compareList(newSeedList, mapList)

    
    print("Result : " ,newSeedList)



def compareList(seedList, mapList):
    newSeedList = seedList
    count = 0

    for list in mapList:
        #print("Numbers Beeing Processed : " ,list)
        sum = int(list[1]) - int(list[0])
        #print("Difference: ", sum)
        seedCount = 0  
        
        for seed in seedList:
                      
            count = 0
            foundMatch = False
            #print("Current Seed: " , seed)
            for _ in range(int(list[2])):
                if int(seed) == int(list[1]) + count:
                    print("This: " ,int(list[1]) + count, "Into : ",(int(list[1]) + count - sum))
                    newSeedList[seedCount] = (int(list[1]) + count - sum)
                    print("New Seed : " ,int(list[1]) + count - sum)               
                    break
                count+=1
        
            seedCount+=1

            
    print("New Seed List : " , newSeedList)
    return newSeedList.copy()




def treatCoordinates(rawCoord):
    lineBuffer =[]
    treatedCoordinates = []
    #print(rawCoord)
    for lines in rawCoord:
        lines = lines.strip()
        lineBuffer = lines.split(" ")
        treatedCoordinates.append(lineBuffer.copy())
        lineBuffer.clear()
    
    return treatedCoordinates

def generateCoordinates(fileQ):
    coordinateList = []
    counting = False
    for i in range(len(list(fileQ.queue))):
        line = fileQ.get()
        
        if line != "\n":
            #print(line[0], counting, )
            if line[0].isdigit():
                coordinateList.append(line)
                counting = True
            elif line[0].isdigit() == False and counting == True:
                return coordinateList
    return coordinateList
    
def createSeedList(fileQ):
    seedList = []
    seedList = fileQ.get()
    seedList = seedList.split(":")[1]
    seedList = seedList.strip().split(" ")
    
    return seedList


main()