import re

def getData(path):
    with open(path, "r") as file:
        return file.readlines()
    
def transformToDotsAndIDs(disk):
    result = []
    IDcount = '0'
    isFreeSpace = False
    for i in range(len(list(disk))):
        if not isFreeSpace:
            for j in range(int(disk[i])):
                result.append(IDcount)
            IDcount = str(int(IDcount)+1)
            isFreeSpace = True
        else:
            for j in range(int(disk[i])):
                result.append(".")
            isFreeSpace = False
    return result

def compress(disk):
    compressedDisk = []
    dotCount = disk.count('.')
    swappedCount = 0
    diskWithoutDots = []
    for i in range(len(disk)):
        if disk[i] != '.':
            diskWithoutDots.append(disk[i])

    for i in range(len(disk) - dotCount):
        if disk[i] == '.':
            compressedDisk.append(diskWithoutDots[-1-swappedCount])
            swappedCount += 1
        else:
            compressedDisk.append(disk[i])
    for i in range(dotCount):
        compressedDisk.append(".")
    return compressedDisk

def checksum(disk):
    return sum([int(disk[i]) * i for i in range(len(disk) - disk.count('.'))])

def main():
    data = getData("day9/input.txt")
    print(checksum(compress(transformToDotsAndIDs(data[0]))))
main()