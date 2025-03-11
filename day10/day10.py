from itertools import chain
import timeit

def getSurroundings(position, trailmap, dimSize):
    neighbours = []
    if position%dimSize < dimSize-1:
        neighbours.append(trailmap[position+1])
    if position%dimSize > 0:
        neighbours.append(trailmap[position-1])
    if position//dimSize < dimSize-1:
        neighbours.append(trailmap[position + dimSize])
    if position > dimSize - 1:
        neighbours.append(trailmap[position - dimSize])
    return neighbours

def findSummit(position, trailmap, dimSize):
    summits = []
    if trailmap[position][1] == 9:
        summits.append(position)
        return summits
    else:
        neighbours = getSurroundings(position, trailmap, dimSize)
        heights = [x[1] for x in neighbours]
        if trailmap[position][1]+1 in heights:
            for n in neighbours:
                if n[1] == trailmap[position][1]+1:
                    summits.append(findSummit(n[0], trailmap, 48))
    return set(list(chain(*summits)))

def main():
    trailmap = [(i-i//49, int(h)) for i, h in enumerate(open("day10/input.txt", "r").read()) if h != '\n']
    summits = []
    for index, item in enumerate(trailmap):
        #print(index)
        if item[1] == 0:
            summits.append(findSummit(index, trailmap, 48))
    #print(len(list(chain(*summits))))

def estimate_distance():
    main()

#num_iterations = 1000  # or even bigger number
#time_taken = timeit.timeit(estimate_distance, number=num_iterations)
#average_time_per_iteration = time_taken / num_iterations
#print(average_time_per_iteration)

'''def aoc10():
    M = {(i,j):int(c) for (i,l) in enumerate(open("day10/test.txt")) for (j,c) in enumerate(l.strip())}   # the map
    print(M)
    N = {(i,j):{(i-1,j), (i+1,j), (i,j-1), (i,j+1)} & M.keys() for (i,j) in M}
    print(N)                         # neighbors
    p = lambda s: [s] if M[s]==9 else sum([p(n) for n in N[s] if M[n]==M[s]+1], [])                    # list paths
    print(p)
    print(sum(len(set(p(c))) for c in M if M[c]==0))      # part 1, count trailheads
aoc10()'''