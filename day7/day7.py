

def check(goal, numbers, currentResult, solved):
    
    if (not solved) and len(numbers)>0:
        for operator in ["+", "*", "||"]:
            if operator == "+" and not solved:
                currentResultAdd = currentResult + int(numbers[0])

                if currentResultAdd == goal:
                    solved = True
                else:
                    solved = check(goal, numbers[1:], currentResultAdd, solved)
            elif operator == "*" and not solved:
                currentResultMultiply = currentResult * int(numbers[0])
                if currentResultMultiply == goal:
                    solved = True
                else:
                    solved = check(goal, numbers[1:], currentResultMultiply, solved)
            elif not solved:
                currentResultConcat = int(str(currentResult) + numbers[0])
                if currentResultConcat == goal:
                    solved = True
                else:
                    solved = check(goal, numbers[1:], currentResultConcat, solved)
    elif len(numbers) == 1:
        if goal == currentResult:
            solved = True
    return solved
        

def main():
    results = []
    numbers = []
    score = 0
    with open("day7/input.txt", "r") as file:
        for line in file.readlines():
            results.append(line.split(":")[0])
            numbers.append(line.rstrip("\n").split(":")[1].lstrip(" ").split(" "))
    for i in range(len(results)):
        if check(int(results[i]), numbers[i][1:], int(numbers[i][0]), False):
            score += int(results[i])
    print(score)
main()