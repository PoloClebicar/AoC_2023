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

    '''
    TODO: Parsing the numbers correctly, but making a mistake in conversion is some point
    Follow the conversions to find the erros
    '''
    print("Old Seed List : ", seedList)
    bufferList = []
    newSeedList = []
    #Naming the variables for the seed
    for i in range(int(((len(seedList))/2))):
        seedRangeStart = int(seedList[i *2])
        seedRangeEnd = int(seedList[i *2]) + int(seedList[(i*2) + 1])
        print("Seeds : ", seedRangeStart, seedRangeEnd)

        for mapLists in mapList:
            print("Maps :" ,mapLists)
            #Naming the variables for map
            mapRangeStart = int(mapLists[1])
            mapRangeEnd = int(mapLists[1]) + int(mapLists[2])
            mapKey = int(mapLists[1]) - int(mapLists[0])

            #Check if the seeds and maps intersect

            if mapRangeStart <= seedRangeStart <= mapRangeEnd and mapRangeStart <= seedRangeEnd <= mapRangeEnd:
                #Seed fully inside map range
                #Cover both Start and End of Seed Range converted
                #We remove the Seed Range start from the end to create a Range, and not a end position
                bufferList = [seedRangeStart + mapKey,(seedRangeEnd + mapKey) - seedRangeStart]
                
            elif seedRangeStart <= mapRangeStart <= seedRangeEnd and seedRangeStart <= mapRangeEnd <= seedRangeEnd:
                #Map range fully withing Seeds
                #Create a list with SeedStart -> MapStart -1, 
                #another range from MapStart -> MapEnd, 
                #another from Mapend + 1 -> Seed End
                bufferList = [seedRangeStart, ((mapRangeStart - 1) - seedRangeStart),
                              (mapRangeStart + mapKey), (mapRangeEnd + mapKey),
                              (mapRangeEnd + 1), (seedRangeEnd)]
            elif mapRangeStart <= seedRangeStart <= mapRangeEnd and not (mapRangeStart <= seedRangeStart <= mapRangeEnd):
                #Seed start within but seed end out
                #Create a range with Start converted -> Maprange end, maprangend +1 -> normal Seed end 
                bufferList = [(seedRangeStart + mapKey), (mapRangeEnd - seedRangeStart),
                              (mapRangeEnd + 1), (seedRangeEnd)]
            elif not(mapRangeStart <= seedRangeStart <= mapRangeEnd) and mapRangeStart <= seedRangeStart <= mapRangeEnd:
                #Seed start out but seed end within
                #Create a range SeedStartNormal -> SeedStart -1,
                #SeedStart Converted ->imapRangeEndCoverted,
                bufferList = [(seedRangeStart), (mapRangeStart - 1),
                              (mapRangeStart + mapKey),(seedRangeEnd + mapKey - seedRangeStart)]
            else:
                #The ranges do not overlap
                bufferList = [(seedRangeStart), (seedRangeEnd - seedRangeStart)]

        for itens in bufferList:
            newSeedList.append(itens)

        bufferList.clear() 

    print("New Seed List : " ,newSeedList)
    return newSeedList 

        
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