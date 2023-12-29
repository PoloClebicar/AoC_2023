
def main():   
    resultado = 0
    sum = 0
    file = open("/workspaces/AoC_2023/day1/part2/list.txt", "r")
    
    #fileList = file.readlines()
    replacedFile = []

        #this fells wrong but it works I guess
    for lines in file:
        replacedFile.append(lines.replace("one", "o1e").replace("two", "t2o").replace("three", "thr3e").replace("four", "fo4r").replace("five", "fi5e").replace("six", "s6x").replace("seven", "sev7n").replace("eight", "eig8t").replace("nine", "ni9e"))
        #print(replacedFile)    
    
    for rows in replacedFile:
        #print(find_numbers(rows))
        resultado += find_numbers(rows)
    
    print(resultado)
    
    

def find_numbers(lines):
    numberList = []
    for letters in lines:
        if letters.isdigit():
            numberList.append(letters)

            if len(numberList) == 1:
                sum = numberList[0] + numberList[0]
            else:
                sum = numberList[0] + numberList[len(numberList) - 1]
    
    return int(sum)

    

main()