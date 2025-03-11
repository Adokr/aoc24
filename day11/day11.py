def aoc11():
    initial = open("day11/test.txt", "r").read()
    augmentation = initial.split()
    print(augmentation)
    count = 0
    while count < 25:
        newAugmentation = []
        for stone in augmentation:
            if int(stone) == 0:
                newAugmentation.append('1')
            elif len(stone)%2 == 0:
                newAugmentation.append(stone[0:int(len(stone)/2)])
                newAugmentation.append(n.lstrip('0') if set(n:=stone[int(len(stone)/2):][:])!= {'0'} else '0')
            else:
                newAugmentation.append(str(int(stone)*2024))
        augmentation = newAugmentation
        print(count)
        count += 1

    print(len(augmentation))

aoc11()