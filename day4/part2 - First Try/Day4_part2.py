import queue

result = 0

def card_fun(lines, cards, lineList, result):
    #print(lines)
    result+=1
    winNumList =[]
    haveNumList = []
    counter = 0

     #clears winNumList and haveNumList
    winNumList.clear()
    haveNumList.clear()

    cardId = lines.split(":")[0]
    cardId = cardId.split(" ", 1)
    cardId = cardId[1].strip()
    cardId = int(cardId)
    
    rawWinningNum = lines.split(":")[1].split("|")[0]
    rawHaveNum = lines.split(":")[1].split("|")[1]
     #print(rawWinningNum)

     #remove spaces to the left
    rawWinningNum = rawWinningNum.strip()
    rawHaveNum = rawHaveNum.strip()

     #pass the number to the right list
    for i in range(len(rawWinningNum.split(" "))):
         if rawWinningNum.split(" ")[i] != '':
              winNumList.append(rawWinningNum.split(" ")[i])

    for i in range(len(rawHaveNum.split(" "))):
          if rawHaveNum.split(" ")[i] != '':
               haveNumList.append(rawHaveNum.split(" ")[i].removesuffix("\n"))

               
    for win in winNumList:
         for have in haveNumList:
              if win == have:
                #add new card to queue
                    cards.put(lineList[cardId + counter])
                    counter+=1
                    print("Current Card: ", cardId)
                    
                    
                    
                   
    return result

    


def main(result):
     cards = queue.Queue()
     lineList = []
     
     file = open("/workspaces/AoC_2023/day4/part2 - First Try/list.txt", "r")

     for lines in file:
          cards.put(lines)
          lineList.append(lines)
     #print(list(cards.queue))

     while not cards.empty():
          result = card_fun(cards.get(), cards, lineList,result)
          #print("Calling")

     print(result)



main(result)