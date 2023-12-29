def main():
    #Numbner of matches in a card
    matchCount = 0

    result = 0

    winNumList =[]
    haveNumList = []

    multList = []
  

    file = open("/workspaces/AoC_2023/day4/part2 - Better/list.txt", "r")

    for _ in file:
         multList.append(1)
    
         
    file = open("/workspaces/AoC_2023/day4/part2 - Better/list.txt", "r")
    
    for lines in file:
        
        matchCount = 0
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
                       #Generate a list of multipliers, and multiply them with the correct line
                       multList[cardId + matchCount] = multList[cardId + matchCount] + 1 * multList[cardId - 1]
                       
                       matchCount+=1
         #The list now holds the number of card in each position, just add them up
        result += multList[cardId - 1]            

         

    print(result)
main()