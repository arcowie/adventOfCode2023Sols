#!/usr/bin/env python3

input = "/home/arcowie/projects/adventOfCode2023/day5/inputDay5.txt"

class seedMap:
    def __init__(self, seedNum):
        self.smap = {}
        self.smap["seed"]=seedNum
        self.smap["soil"]=None
        self.smap["fertilizer"]=None
        self.smap["water"]=None
        self.smap["light"]=None
        self.smap["temperature"]=None
        self.smap["humidity"]=None
        self.smap["location"]=None

    def updateMap(self, field, value):
        self.smap[field]=value




seedDict = {}

def procLine(line, src, dest):
    line = line.split("\n")[0].split(" ")
    desStart = int(line[0])
    srcStart = int(line[1])
    rng = int(line[2])
    #destEnd = desStart+rng
    srcEnd = srcStart+rng 
    for key in seedDict:
        if srcStart<=seedDict[key].smap[src] < srcEnd:
            offSet=seedDict[key].smap[src]-srcStart
            seedDict[key].smap[dest]=desStart+offSet

def checkForNoMap(src, dest):
    for key in seedDict:
        if seedDict[key].smap[dest] == None:
            seedDict[key].smap[dest] = seedDict[key].smap[src]

def populateSeedDict(seeds):
    seeds = seeds.split(": ")[1].split(" ") 
    for seed in seeds:
        seedDict[int(seed)] = seedMap(int(seed))

def getLowestLocation():
    lowestLoc=None
    for key in seedDict:
        if lowestLoc == None:
            lowestLoc = seedDict[key].smap["location"]
        else:
            lowestLoc = lowestLoc if lowestLoc <= seedDict[key].smap["location"] else seedDict[key].smap["location"]
      
    return lowestLoc

with open(input, "r") as file:
    file = file.readlines()
    numberOfLines = len(file)
    currentLine = 0
    print(file[122])
    while currentLine<numberOfLines:
        line = file[currentLine]
        if "seeds" in line:
            populateSeedDict(line)
            currentLine+=1
        elif "map" in line:
            source = line.split("-")[0]
            destination=line.split("-")[2].split(" ")[0]
            currentLine+=1
            line=file[currentLine]
            while line != "\n":
                procLine(line, source, destination)
                currentLine+=1
                checkForNoMap(source, destination)
                if currentLine>=197:
                    break
                line = file[currentLine]
            
        elif "\n" == line:
            currentLine+=1
    print(getLowestLocation())

   

                    



