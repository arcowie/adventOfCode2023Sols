#!/usr/bin/env python3

copyCount = {}
input = "/home/arcowie/projects/adventOfCode2023/day4/inputDay4.txt"

def procLine(line):
    matchNum = 0
    temp = line.split(":")[1]
    temp = temp.split("\n")[0]
    winNumbs = temp.split("|")[0]
    winNumbs = winNumbs.split(" ")
    while "" in winNumbs:        
        winNumbs.remove("")
    numsToCheck = temp.split("|")[1]
    numsToCheck = numsToCheck.split(" ")
    while "" in numsToCheck:
        numsToCheck.remove("")
    for num in winNumbs:
        if num in numsToCheck:
            matchNum+=numsToCheck.count(num)
            
    return matchNum


def addToCopyDict(num, currentLine):
    for i in range(1, result+1):
        copyCount[currentLine+i]+=1

with open(input, "r") as file:
    sum = 0
    result = 0
    currentLine = 0
    lines = file.readlines()
    numLines = len(lines)
    for x in range(numLines):
        copyCount[x]=0
    for line in lines:
        sum+=1
        result = procLine(line)
        addToCopyDict(result, currentLine)
        sum=sum+result
        if copyCount[currentLine]==0:
            currentLine+=1
            continue
        else:
            for copy in range(copyCount[currentLine]):
                result = procLine(line)
                addToCopyDict(result, currentLine)
                sum=sum+result
            currentLine+=1
        
    print(sum)