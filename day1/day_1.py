
list1 = []
list2 = []
with open("day1/input.txt", "r") as file:
    for line in file.readlines():
        line = line.split('   ')
        list1.append(int(line[0]))
        list2.append(int(line[1].strip("\n")))
    #print(list1)

def sort(list_to_be_sorted):
    is_sorted = False
    not_swapped_count = 0
    while not is_sorted:
        for i in range(len(list_to_be_sorted)-1):
            if list_to_be_sorted[i] > list_to_be_sorted[i+1]:
                list_to_be_sorted[i], list_to_be_sorted[i+1] = list_to_be_sorted[i+1], list_to_be_sorted[i]
            else:
                not_swapped_count += 1
        if not_swapped_count + 1 == len(list_to_be_sorted):
            is_sorted = True
        else: 
            not_swapped_count = 0
    sorted_list = list_to_be_sorted
    
    return sorted_list

def calculate_distances(listx, listy):
    total_distance = 0
    for i in range(len(listy)):
        total_distance += abs(listx[i] - listy[i])
    return total_distance

def count_instances(list, element):
    count = 0
    for el in list:
        if el == element:
            count += 1
    return count

def calculate_similarity(listx, listy):
    total_similarity = 0
    for el in listx:
        total_similarity += el*count_instances(listy, el)
    return total_similarity

#print(count_instances([1, 2, 3, 4, 1, 2, 1, 1], 1))
#print(calculate_distances(sort(list1), sort(list2)))
print(calculate_similarity(sort(list1), sort(list2)))

exit()
