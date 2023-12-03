#!/usr/bin/env python3

input = "/home/arcowie/projects/adventOfCode2023/day2/inputDay2.txt"

def parseLine(line):
    refCubeNum = {
    "red" : 1,
    "green" : 1,
    "blue" : 1
    }
    pow=1
    gameNum=int(line.split(":")[0].split(" ")[1])
    game = line.split(": ")[1].split("; ")
    for pull in game:
        pull=pull.replace(",", "")
        pull=pull.split(" ")
        for x in range(1, len(pull), 2):
            color=pull[x]
            numberPulled=int(pull[x-1])
            refCubeNum[color] =  numberPulled \
                if numberPulled>=refCubeNum[color] else refCubeNum[color]
    for key in refCubeNum:
        pow=pow*refCubeNum[key]
    return pow

    


with open(input, "r") as file:
    sum = 0
    for line in file:
        line = line.split("\n")[0]
        sum = sum + parseLine(line)
    print(sum)