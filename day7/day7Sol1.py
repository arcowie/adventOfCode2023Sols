#!/usr/bin/env python3
from functools import cmp_to_key

input = "/home/arcowie/projects/adventOfCode2023/day7/inputDay7.txt"
inputTest = "/home/arcowie/projects/adventOfCode2023/day7/inputTest.txt"

handDict = {"fiveOfAKind" : [],
            "fourOfAKind" : [],
            "fullHouse" : [],
            "threeOfAKind" : [],
            "twoPair" : [],
            "onePair" : [],
            "highCard" : []}

faceCardToNum = {"A" : 14, 
                 "K" : 13, 
                 "Q" : 12, 
                 "J" : 1,
                 "T" : 10}


def getCardValue(card):
    faceCards=["A","K","Q","J","T"]
    if card in faceCards:
        return faceCardToNum[card]
    else:
        return int(card)

def compare(hand1, hand2):
    hand1=hand1[0]
    hand2=hand2[0]
    cardH1=None
    cardH2=None
    for x in range(len(hand1)):
        cardH1 = getCardValue(hand1[x])
        cardH2 = getCardValue(hand2[x])
        if cardH1 == cardH2:
            continue
        elif cardH1 > cardH2:
            return -1
        elif cardH1 < cardH2:
            return 1


def procHands(allHandsLst):
    for hand in allHandsLst:
        hand = hand.split("\n")[0].split(" ")
        count = [hand[0].count(x) for x in hand[0]]
        if 5 in count:
            handDict["fiveOfAKind"].append(hand)
        elif 4 in count:
            handDict["fourOfAKind"].append(hand)
        elif 3 in count and 2 in count:
            handDict["fullHouse"].append(hand)
        elif 3 in count:
            handDict["threeOfAKind"].append(hand)
        elif count.count(2) == 4:
            handDict["twoPair"].append(hand)
        elif count.count(2) == 2:
            handDict["onePair"].append(hand)
        else:
            handDict["highCard"].append(hand)


def getTotWins(maxRank):
    handsLst = []
    total = 0
    handsLst.append(handDict["fiveOfAKind"])
    handsLst.append(handDict["fourOfAKind"])
    handsLst.append(handDict["fullHouse"])
    handsLst.append(handDict["threeOfAKind"])
    handsLst.append(handDict["twoPair"])
    handsLst.append(handDict["onePair"])
    handsLst.append(handDict["highCard"])
    for i in range(len(handsLst)):
        if handsLst[i] == []:
            continue
        else:
            for k in range(len(handsLst[i])):
                total = total + int(handsLst[i][k][1])*maxRank
                maxRank+=-1
    return total







def main():
    with open(input, "r") as file:
        allHandsLst = file.readlines()
        maxRank = len(allHandsLst)
    procHands(allHandsLst)
    for key in handDict:
        if len(handDict[key]) > 1:
            handDict[key]=sorted(handDict[key], key=cmp_to_key(compare))
    print(getTotWins(maxRank))
    






if __name__ == "__main__":
    main()