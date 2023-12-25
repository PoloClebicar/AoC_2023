file = open("/workspaces/AoC_2023/day2/part1/list.txt", "r")


#I am very sleepy and this is a mess, but it works!
result = 0


gameID = []
gameNum = []
for lines in file:
    gameID = lines.split(":")[0].split(" ")[1]
    gameNum = lines.split(":")[1].split(";")
    isPossible = 0
    #print("GAME SPLIT_____________")
    isPossible = False
    for sets in gameNum:
        singleGame = sets.split(",")
        #print(singleGame)
        
        red = 0
        green = 0
        blue = 0

        for games in singleGame:
            cubeNumber = games.split(" ")[1]
            cubeColor = games.split(" ")[2]
            #print(cubeNumber, cubeColor)

            match cubeColor[0]:
                case "r":
                    red = int(cubeNumber)
                case "g":
                    green = int(cubeNumber)
                case "b":
                    blue = int(cubeNumber)

        #print(red, green, blue)          

        if red <= 12 and green <= 13 and blue <= 14:
            #print("Hey____________________________")
            isPossible = True
        else:
            #print("Nay____________________________")
            isPossible = False
            break
    if isPossible == True:
        result += int(gameID)

print(result)


