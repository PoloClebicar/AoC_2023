def main():
    file = open("/workspaces/AoC_2023/day3/part2/list.txt", "r")
  
    lineCount = 0
    lineList = []
    partList =[]
    numBuffer = ""
    indexBuffer = []
    bufferList = []
    adjecentPartCount = 0
    gearList = []
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
                     adjecentPartCount = 0
                     
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
                                            bufferList.append(numBuffer)
                                            adjecentPartCount +=1
                                            break                                            
                                        j+=1
                                    numBuffer = ""
                                    indexBuffer = []                        
                        i+=1

                     #Out of the Symbol Loop
                     if adjecentPartCount == 2:
                         print(bufferList[0], bufferList[1])
                         gearList.append(int(bufferList[0]) * int(bufferList[1]))
                     else:
                         for _ in range(len(bufferList)):
                             partList.append(bufferList[_])
                         
                    
                     bufferList.clear()

    print(gearList, partList)

    for _ in range(len(gearList)):
        result += gearList[_]
    
    
    print(result)

main()