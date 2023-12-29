def main():
    #Numbner of matches in a card
    matchCount = 0

    result = 0

    winNumList =[]
    haveNumList = []

    file = open("/workspaces/AoC_2023/day4/part1/list.txt", "r")
    
    for lines in file:
        #print("NEW CARD")
        matchCount = 0
        #clears winNumList and haveNumList
        winNumList.clear()
        haveNumList.clear()

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
                       matchCount+=1

        match matchCount:
             case 0:
                  result+=0
             case 1:
                  result+=1
             case 2:
                  result+=2
             case _:
                  result += pow(2, matchCount -1)
            
                  



    print(result)  

main()