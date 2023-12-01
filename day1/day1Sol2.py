#!/usr/bin/env python3

fileName="input.txt"

def findNum(line):
    digit = ""
    index = 0
    for char in line:
        if char.isdigit():
            wordIndex, wordDig = checkForWordDigit(line, "left")
            if wordIndex != None:
                if index < wordIndex:
                    digit=digit+char
                else:
                    digit=digit+wordDig
            else:
                digit=digit+char
            break
        index+=1

    index=len(line)-1
    for char in line[::-1]:
        if char.isdigit():
            wordIndex, wordDig = checkForWordDigit(line, "right")
            if wordIndex != None:
                if index > wordIndex:
                    digit=digit+char
                else:
                    digit=digit+wordDig
            else:
                digit=digit+char
            break
        index+=-1
    calValue=digit[0]+digit[-1]
    return int(calValue)


def checkForWordDigit(line, pos):
    line=line.lower()
    listToSubIndex=[]

    substStrings=[
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9")
    ]

    origline=line
    for text, num in substStrings:
        if pos == "left":
            index = line.find(text)
            reverse = False
        else:
            try:
                reverse = True
                index = line.rindex(text)
            except ValueError:
                continue
        if index !=-1:
            listToSubIndex.append((index, text, num))
    listToSubIndex=sorted(listToSubIndex, reverse=reverse)
    
    if len(listToSubIndex) > 0:
        return listToSubIndex[0][0], listToSubIndex[0][2]
    else:
        return None, None

with open(fileName, "r") as file:
    sum=0
    for line in file:
        sum=sum+findNum(line)
    print(f"Sum: {sum}")