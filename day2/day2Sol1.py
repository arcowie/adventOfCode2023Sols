#!/usr/bin/env python3

input = "/home/arcowie/projects/adventOfCode2023/day2/inputDay2.txt"
refCubeNum = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

def evalPull(pull):
    pull=pull.replace(",", "")
    pull=pull.split(" ")
    
    for x in range(1, len(pull), 2):
        color=pull[x]
        numberPulled=pull[x-1]
        if refCubeNum[color]<int(numberPulled):
            return False
            

    return True

def parseLine(line):
    gamePossible=True
    gameNum=int(line.split(":")[0].split(" ")[1])
    game = line.split(": ")[1].split("; ")
    for pull in game:
        if evalPull(pull): 
            continue
        else:
            return 0
    return gameNum

    


with open(input, "r") as file:
    sum = 0
    for line in file:
        line = line.split("\n")[0]
        sum = sum + parseLine(line)
    print(sum)