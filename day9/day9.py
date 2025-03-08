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

def findLeftmostFreeSpace(disk, size, fileID):
    freeSpaceID = None
    freeSpaceSize = 0
    freeSpaceCount = 0
    fileCount = 0
    freeSpaceSeenAlready = False
    fileSeenAlready = False

    for i in range(len(disk)):
        if i >= fileID:
            break

        if disk[i] == '.' and not freeSpaceSeenAlready:
            freeSpaceCount += 1
            freeSpaceSeenAlready = True
            fileSeenAlready = False
            for j in range(i, len(disk)):
                if disk[j] == ".":
                    freeSpaceSize += 1
                else:
                    break
            if freeSpaceSize >= size:
                freeSpaceID = i
                break

        elif disk[i] != '.' and not fileSeenAlready:
            fileCount += 1
            freeSpaceSeenAlready = False
            fileSeenAlready = True
        freeSpaceSize = 0
    return freeSpaceID

def getFileID(disk, file):
    for i in range(len(disk)):
        if disk[i] == file:
            return i
    return None

def moveFiles(disk):
    alreadyMoved = set([])
    for i in range(int(max(disk)), 0, -1):
        print(i)
        fileToMove = i
        if fileToMove not in alreadyMoved:
            fileID = getFileID(disk, str(fileToMove))
            fileToMoveSize = disk.count(str(i))
            freeSpaceID = findLeftmostFreeSpace(disk, fileToMoveSize, fileID)
            if  freeSpaceID is not None:
                disk[freeSpaceID:(freeSpaceID+fileToMoveSize)] = [str(fileToMove)]*fileToMoveSize
                disk[fileID:fileToMoveSize+fileID] = ['.']*fileToMoveSize
        alreadyMoved.add(fileToMove)
    return disk        

def checksum(disk):
    result = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            result += i*int(disk[i])
    return result
def main():
    data = getData("day9/input.txt")
    print(checksum(moveFiles(transformToDotsAndIDs(data[0]))))
main()