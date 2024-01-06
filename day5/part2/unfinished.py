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
    for i in range(int(len(seedList)/2)):
        if seedList[i * 2] <= res:
            res = seedList[i * 2]
    

    return res


def compareList(seedList, mapList):
    newSeedList = []
    
    #print(seedList, mapList)
    for i in range(int(len(seedList)/2)):
        seedStart = int(seedList[i*2])
        seedRange = int(seedList[(i*2)+1])
        seedEnd = int(seedStart) + int(seedRange)

        bufferList = [seedStart, seedRange]
        
        #For each map range in mapList, we check and update the list
        for maps in mapList:
            mapStart = int(maps[1])
            mapsEnd = int(maps[1]) + int(maps[2])
            mapRange = int(maps[2])
            mapsKey = int(maps[0]) -int(maps[1])

            matchFound = False


            #Seeds fully contained inside map
            if mapStart <= seedStart <= mapsEnd and mapStart <= seedEnd <= mapsEnd:
                #Just Convert the seed start
                print("Key : ", mapsKey, "Case 1")
                bufferList = [seedStart + mapsKey, seedRange]
                print(bufferList)
                matchFound = True
                break
            
            #Maps fully contained inside key
            elif seedStart <= mapStart <= seedEnd and seedStart <= mapsEnd <= seedEnd:
                #create 3 ranges
                #seedStart -> Mapstart -1
                #mapstart + key -> map end + key
                #map end +1 -> seedEnd
                print("Key : ", mapsKey, "Case 2")
                bufferList = [seedStart, (mapStart - 1) - seedStart,
                              mapStart + mapsKey, mapRange,
                              mapsEnd + 1, seedEnd - mapsEnd + 1]
                print(bufferList)
                matchFound = True
                break
            
            #Seed starts out but end within
            elif seedStart < mapStart and mapStart <= seedEnd <= mapsEnd:
                #create 2 ranges
                #Seedstart -> mapstart -1
                #map start converted -> seed end
                print("Key : ", mapsKey, "Case 3")
                bufferList = [seedStart, (mapStart - 1) - seedStart,
                              mapStart + mapsKey, mapsEnd - seedEnd + 1]
                print(bufferList)
                matchFound = True
                break
                
            #Seed starts in but ends out    
            elif mapStart <= seedStart <= mapsEnd and seedEnd > mapsEnd:
                #create two ranges
                #Seed start converted -> map end
                #map end + 1, seed end
                print("Key : ", mapsKey, "Case 4")
                bufferList = [seedStart + mapsKey, mapsEnd - seedStart,
                              mapsEnd + 1, seedEnd - mapsEnd + 1]
                print(bufferList)
                matchFound = True
                break

        for buffers in bufferList:
            newSeedList.append(buffers)
        bufferList.clear()

        
            
        
    print(newSeedList)
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