
def main():   
    resultado = 0
    file = open("/workspaces/AoC_2023/Day1/list.txt", "r")
    
    #fileList = file.readlines()
   
    for lines in file:
        resultado += find_numbers(lines)
    
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