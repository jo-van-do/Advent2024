# Open data
reports = []
total = 0

with open('day2\data2.txt', 'r') as f:
    for line in f.readlines():
        reports.append(list(map(int, line.split(' '))))
f.close()


def inc_or_dec(report):
    """Checks if report numbers are all increasing or decreasing
    """
    inc_or_dec = False
    
    if all(report[i] <= report[i + 1] for i in range(len(report) - 1)):
        inc_or_dec = True
    elif all(report[i] >= report[i + 1] for i in range(len(report) - 1)):
        inc_or_dec = True
    
    return inc_or_dec


def is_gradual(report):
    """Checks if adjacent report numbers difference => 1 and <= 3 
    """
    gradual = True
    
    for first, second in zip(report, report[1:]):
        if abs(second - first) not in range(1,4):
            gradual = False
    
    return gradual

for report in reports:
    if inc_or_dec(report) and is_gradual(report):
        total += 1

print(total)
