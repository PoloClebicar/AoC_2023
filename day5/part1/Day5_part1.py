import queue

def main():
    print("HEllo")
    file = open("/workspaces/AoC_2023/day5/part1/list.txt", "r")

    lineQueue = queue.Queue()

    seedList = []
    mapList = []
    
    startPosList =[]
    keyList = []

    for _ in file:
        lineQueue.put(_)

    seedList = lineQueue.get().split(":")[1].strip().split(" ")

    while not lineQueue.empty():
        
        rawMapList = create_raw_list(lineQueue)
        mapList = split_raw_list(rawMapList)

        for i in range(len(mapList)):
            startPosList, directionPosList = generate_search_list(mapList[i])
            seedList = create_new_seed_list(seedList, startPosList, directionPosList)
           
        print(seedList)

def create_new_seed_list(seedList, destinationRange, sourceRange):
    proccesList =[]    
    for seed in seedList:
        matchFound = False
        i=0        
        for source in sourceRange:
            #print(seed, source)
            if int(seed) == int(source):              
                proccesList.append(source + (destinationRange[0] - sourceRange[0]))
                matchFound = True
                break
            i+=1
        if matchFound == False:
            proccesList.append(seed)
    #print(proccesList)
    return proccesList
                
#Now we must generate the full list of positions
def generate_search_list(mapListPosition):
    
    startPosList =[]
    directionPosList = []
    for i in range(len(mapListPosition)):
        startPos = int(mapListPosition[0])
        directionPos = int(mapListPosition[1])
        key = int(mapListPosition[2])

    for i in range(key):
            startPosList.append(startPos + i)
            directionPosList.append(directionPos + i)
    
    '''print("SEARCH LIST___________________________")
    print(startPos, directionPos, key)'''
    return startPosList, directionPosList

#Split the info into a list of lists
def split_raw_list(rawMapList):
    #Process the values into a list of list
    #One list contain the values already split, and the other contain thoses lists
    #that way we can process them one at a time easily
    
    mapList =[]
    mapBook = []

    for lines in rawMapList:
        lines = lines.strip()
        mapBook = lines.split(" ")
        mapList.append(mapBook.copy())
    mapBook.clear()
    
    return mapList 
    
#split the raw info into the usefull parts
def create_raw_list(lineQueue):
    #Takes the queue and process it
    #Find the next line of instructions, puts the numbers on a list and returns that list
    currentNumList = []
    while not lineQueue.empty():
        buffer = lineQueue.get()
        if buffer[0].isdigit():
            currentNumList.append(buffer)
        elif len(currentNumList) != 0:
            return currentNumList
    
    return currentNumList 


main()


