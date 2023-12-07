#!/usr/bin/env python3
from math import sqrt, ceil
input = "/home/arcowie/projects/adventOfCode2023/day6/inputDay6.txt"
#input = "/home/arcowie/projects/adventOfCode2023/day6/testInput.txt"










def evalRace(time, dist):
    holdTime = 0
    win = 0
    while holdTime <=time:
        if holdTime*(time-holdTime) > dist:
            win+=1
        holdTime+=1
    return win



def main():
    with open(input, "r") as file:
        file = file.readlines()
        time = file[0]
        dist = file[1]
    time = time.split(": ")[1].split("\n")[0].split(" ")
    time = [int(x) for x in time if x != ""]
    dist = dist.split(": ")[1].split(" ")
    dist = [int(x) for x in dist if x != ""] 
    x=0
    margin=1
    while x < len(time):
        result = evalRace(time[x], dist[x])
        x+=1
        margin = margin*result
    print(margin)

    time, dist = [60947882, 475213810151650]
    disc=sqrt(time ** 2 - (4 * dist))
    print(int((time + disc) / 2)-ceil((time - disc) / 2))


if __name__ == "__main__":
    main()

