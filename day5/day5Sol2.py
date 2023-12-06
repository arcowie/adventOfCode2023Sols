#!/usr/bin/env python3

input = "/home/arcowie/projects/adventOfCode2023/day5/inputDay5.txt"
#input = "/home/arcowie/projects/adventOfCode2023/day5/testInput.txt"


def parseInput(file):
    seeds = file.pop(0).split(": ")[1].split("\n")[0].split(" ")
    seeds = [[int(seeds[x]), int(seeds[x])+int(seeds[x+1])] for x in range(0,len(seeds), 2)]
    mapAll = []
    currentLine = 0
    fileLen=len(file)
    while currentLine<fileLen:
        line = file[currentLine] 
        if "map" in line:
            temp=[line]
            currentLine+=1
            line=file[currentLine]
            while line != "\n":
                temp.append(line.split("\n")[0].split(" "))
                currentLine+=1
                try:
                    line=file[currentLine]
                except:
                    print("at EOF breaking out of while.")
                    break
            mapAll.append(temp)
        elif line == "\n":
            currentLine+=1
            line=file[currentLine]
    return seeds, mapAll


def runMap(srcRanges, mapAll):
    for map in mapAll:
        print(f"Running map: {map[0]}")
        map = map[1::]
        i=0
        startLenSrcRanges = len(srcRanges)
        while i < startLenSrcRanges:
            k = 0
            while k < len(map):
                line = map[k]
                dest, src, rng = [int(x) for x in line]
                begin, end = srcRanges[i]
                if src <= begin and (src+rng) >= begin:
                    offset = begin-src
                    srcRanges[i][0] = dest + offset
                    if (src+rng) >= end:
                        srcRanges[i][1] = dest + offset + (end-begin)
                        break
                    else: 
                        srcRanges[i][1] = dest + rng - 1
                        newBegin = src + rng
                        srcRanges.append([newBegin,end])
                        break
                elif src > begin and src <= end:
                    newBegin = srcRanges[i][0]
                    newEnd = newBegin + (src-begin-1)
                    srcRanges.append([newBegin, newEnd])
                    srcRanges[i][0] = dest
                    if (src+rng) >= end:
                        srcRanges[i][1] = dest + (end-src)
                        break
                    else:
                        srcRanges[i][1] = dest + rng - 1
                        newBegin = src + rng 
                        srcRanges.append([newBegin, end])
                        break
                k+=1
            i+=1
    return srcRanges

def main():
    seeds=[]
    mapAll=[]
    with open(input, "r") as file:
        file = file.readlines()
        seeds, mapAll = parseInput(file)
    result = runMap(seeds, mapAll)
    print(min([min(x) for x in result]))


if __name__ == "__main__":
    main()