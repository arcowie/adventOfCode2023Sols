#!/usr/bin/env python3


input = "/home/arcowie/projects/adventOfCode2023/day4/inputDay4.txt"

def procLine(line):
    power = -1
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
            power+=numsToCheck.count(num)
            
    if power > -1:
        return 2**power
    else:
        return 0



with open(input, "r") as file:
    sum = 0
    result = 0
    for line in file:
        for copy in range(result):
            
        result = procLine(line)
        sum=sum+result
    print(sum)