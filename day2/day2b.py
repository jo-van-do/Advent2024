reports = []
total = 0

with open('day2\data2.txt', 'r') as f:
    for line in f.readlines():
        versions = []
        report = list(map(int, line.split(' ')))
        versions.append(report)
        
        for i in range(len(report)):
            new_version = report.copy()
            new_version.pop(i)
            versions.append(new_version)
        
        reports.append(versions)

f.close()


def inc_or_dec(numlist):
    """Checks if report numbers are all increasing or decreasing
    """
    inc_or_dec = False

    if all(numlist[i] <= numlist[i + 1] for i in range(len(numlist) - 1)):
        inc_or_dec = True
    elif all(numlist[i] >= numlist[i + 1] for i in range(len(numlist) - 1)):
        inc_or_dec = True

    return inc_or_dec



def is_gradual(numlist):
    """Checks if adjacent report numbers difference => 1 and <= 3 
    """
    gradual = True
    
    for first, second in zip(numlist, numlist[1:]):
        if abs(second - first) not in range(1,4):
            gradual = False
    
    return gradual

for report in reports:
    for version in report:
        if inc_or_dec(version) and is_gradual(version):
            total += 1
            break

print(total)
