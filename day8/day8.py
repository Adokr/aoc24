from itertools import chain 
import numpy as np

def findAntennas(board, type):
    locations = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == type:
                locations.append([i,j])
    print(locations)
    return locations

def calculateDistance(loc1, loc2):
    return [loc2[0]-loc1[0], loc2[1] - loc1[1]]

def findAntinodes(locations, board):
    antinodes = []
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            dist = calculateDistance(locations[i], locations[j])
            antinodes.append([locations[i][0]-dist[0], locations[i][1]-dist[1]])
            antinodes.append([locations[j][0]+dist[0], locations[j][1]+dist[1]])
    actualAntinodes = []
    for loc in antinodes:
        if loc[0] >= 0 and loc[0] < len(board):
            if loc[1] >= 0 and loc[1] < len(board[0]):
                actualAntinodes.append((loc[0], loc[1]))
    return actualAntinodes #[np.squeeze(i) for i in actualAntinodes]

def main():
    board = []
    antinodes = []
    with open("day8/input.txt", "r") as file:
        for line in file.readlines():
            board.append(list(line.rstrip("\n")))

    for char in set(list(chain(*board))) - {'.'}: 
        antinodes.extend(findAntinodes(findAntennas(board, char), board))

    print(len(set(antinodes)))
main()