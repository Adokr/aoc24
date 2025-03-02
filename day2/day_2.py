def main():
    safe_reports_count = 0
    reports = []
    with open("day2/input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            reports.append(line.strip('\n').split(' '))
    
    for report in reports:
        if is_safe(report):
            safe_reports_count += 1
        elif problem_dampener(report):
            safe_reports_count += 1
    print(safe_reports_count)

def is_safe(report):
    score = 0
    for i in range(len(report)-1):
        if abs(int(report[i]) - int(report[i+1])) > 3:
            break
        elif int(report[i]) > int(report[i+1]):
            score += 1
        elif int(report[i]) < int(report[i+1]):
            score -= 1
    print(score)
    return abs(score) == len(report)-1  

def create_new_report(report, index):
    new_report = []
    for i in range(len(report)):
        if i != index:
            new_report.append(report[i])
    return new_report

def problem_dampener(report):
    did_it_work = False
    for i in range(len(report)):
        new_report = create_new_report(report, i)
        if is_safe(new_report):
            did_it_work = True
            break
    return did_it_work


main()
exit()