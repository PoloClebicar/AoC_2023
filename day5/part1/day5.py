import queue

def main():
    #Set up the Queue 
    fileQ = queue.Queue()

    file = open("/workspaces/AoC_2023/day5/part1/testList.txt", "r")

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

    
    print("Result : " ,checkSmallestNumber(newSeedList))


def checkSmallestNumber(seedList):
    res = int(seedList[0])
    for seeds in seedList:
        if int(seeds) <= res:
            res = int(seeds)

    return res


def compareList(seedList, mapList):
    bufferList = seedList
    i = -1
    print(seedList, mapList)

    for seed in bufferList:
        i+=1
        for maps in mapList:
            if int(maps[1]) <= int(seed) <= int(maps[1]) + int(maps[2]) - 1:                
                bufferList[i] = int(maps[0]) - int(maps[1]) + int(seed)
    
    seedList = bufferList
    #print(seedList)
    return seedList


        
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