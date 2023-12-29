file = open("/workspaces/AoC_2023/day2/part2/list.txt", "r")


#I am very sleepy and this is a mess, but it works!
result = 0


gameID = []
gameNum = []
for lines in file: #FULL GAME
    gameID = lines.split(":")[0].split(" ")[1]
    gameNum = lines.split(":")[1].split(";")
    highRed = 0
    highBlue = 0
    highGreen = 0

    #print("GAME SPLIT_____________")
    isPossible = False
    for sets in gameNum: #GAME SET
        singleGame = sets.split(",")
        #print(singleGame)
        
        red = 0
        green = 0
        blue = 0

        for games in singleGame: #EVERY CUBE MATCH
            cubeNumber = int(games.split(" ")[1])
            cubeColor = games.split(" ")[2]
            #print(cubeColor,cubeNumber)

            
            match cubeColor[0]:
                case "r":
                    if cubeNumber > highRed:
                        highRed = cubeNumber
                case "b":
                    if cubeNumber > highBlue:
                        highBlue = cubeNumber
                case "g":
                    if cubeNumber > highGreen:
                        highGreen = cubeNumber


    result += highGreen * highBlue * highRed

print(result)
