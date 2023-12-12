def main():
    file = open("/workspaces/AoC_2023/Day1/list.txt", "r")
    
    fileList = file.readlines()
    
    i = 0
    for files in fileList:
        print(fileList[i])    #Have the breaking down of the str happen here
        i = i + 1
    

main()