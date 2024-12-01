# Open data
with open('day1\data1.txt', 'r') as f:
    lines = f.read().split('\n')
f.close()

left_nos = []
right_nos = []
total = 0

for line in lines:

    left_nos.append(int(line.split('   ')[0]))
    right_nos.append(int(line.split('   ')[1]))

left_nos.sort()
right_nos.sort()

for i, no in enumerate(left_nos):
    total += abs(no - right_nos[i])

print(total)