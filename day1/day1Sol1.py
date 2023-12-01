#!/usr/bin/env python3

fileName="input.txt"


def findNum(testStr):
    digit = ""
    for char in testStr:
        if char.isdigit():
            digit=digit+char
    calValue=digit[0]+digit[-1]
    return int(calValue)




with open(fileName, "r") as file:
    sum =0
    for line in file:
        sum=sum+findNum(line)
    print(f"Sum: {sum}")


