def main():
    file = open("/workspaces/AoC_2023/day3/part1/list.txt", "r")
  
    lineCount = 0
    lineList = []
    numList =[]
    numBuffer = ""
    indexBuffer = []
    result = 0

    for line in file:
        lineList.append(line)
    
    #Loops over all lines
    for line in lineList:
        lineCount+=1    
        symbolIndex = 0 #Reset Every Line for matching

        #Loop Over Characters
        for character in line:
            symbolIndex +=1

            #Check for symbol
            if character.isalnum() == False and character != "." and character != "\n":                 
                     print("SYMBOL", character, lineCount)
                     
                     #Check adjecent Lines
                     i = -2
                     #Checks previous, current and next line
                     for _ in range(3):                          
                        numberIndex = 0

                        #goes over every character in lines
                        for nCharacter in lineList[lineCount + i]:
                             
                             #ignoes the line break character
                             if nCharacter != "\n":
                                numberIndex+=1

                                #checks if its a number and stores is until a "." or symbol comes, also stores its full index
                                if nCharacter.isdigit():
                                    #print(nCharacter)
                                    numBuffer += nCharacter
                                    indexBuffer.append(numberIndex)
                                    #print(indexBuffer, numBuffer, symbolIndex)

                                #When a number ends
                                elif numBuffer != "":
                                    #print("Hello")
                                    j = 0

                                    #Checks the list for the Index of the number(all digits) againts the Symbol Index
                                    for _ in range(len(indexBuffer)):

                                        #Checks if there is recorded numberIndex on the SymbolIndex and near it(-1,+1), if so, saves that number
                                        if symbolIndex == indexBuffer[j] or symbolIndex - 1 == indexBuffer[j] or symbolIndex + 1  == indexBuffer[j]:
                                            numList.append(numBuffer)
                                            break                                            
                                        j+=1
                                    numBuffer = ""
                                    indexBuffer = []
                        i+=1

    for entries in numList:
        result += int(entries)
    
    print(result)

main()