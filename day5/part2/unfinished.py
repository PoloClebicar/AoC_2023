import queue

def main():
    #Set up the Queue 
    fileQ = queue.Queue()

    file = open("/mnt/c/users/thepo/Documents/GitHub/AoC_2023/Aoc_2023/day5/part2/list.txt", "r")

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
    bufferList = []
    newSeedList = []
    for i in range(int((len(seedList)/2))):
       bufferList.append(seedList[i * 2])
       bufferList.append(seedList[(i * 2) + 1])
       print(bufferList)


       #if Seedlist Start in within range of map list, and if SeedList end is withing range also
       for maps in mapList:
           

           '''
           Figure out hwo to create a new list with the correct ranges #TODO
           '''
           #Check if seedrange start is within maprange
           if int(maps[1]) <= int(bufferList[0]) <= int(maps[1]) + int(maps[2]):
                #Check if the end of the range is within maprange
                if int(maps[1]) <= int(bufferList[0]) + int(bufferList[1]) <= int(maps[1]) + int(maps[2]):
                    print("Seed withing Range", maps)
                else:
                    print("Only Start of Seed within range", maps)

           else:
               print("Seeds Not in range",maps)

          #Check it the range is within seed 
           if int(bufferList[0]) <= int(maps[1]) <= int(bufferList[0]) + int(bufferList[1]):
                #Check if the end of the maprange is within seedrange
                if int(bufferList[0]) <= int(map[1]) + int(maps[2]) <= int(bufferList[0]) + int(bufferList[1]):
                    print("Map withing SeedRange", maps)
                else:
                    print("Only Start of Map within range", maps)

           else:
               print("Map Not in range",maps)


       bufferList.clear()

    
    print(mapList) 

        
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