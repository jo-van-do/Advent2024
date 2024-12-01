with open('day1\data1.txt', 'r') as f:
    lines = f.read().split('\n')
f.close()

left_nos = []
right_nos = []
total_left = 0
total_right = 0
sim_score = 0

for line in lines:

    left_nos.append(int(line.split('   ')[0]))
    right_nos.append(int(line.split('   ')[1]))
    
no_dict = {key: [] for key in set(left_nos)}

for key in no_dict:
    total_left = 0
    total_right = 0
    for no in left_nos:
        if no == key:
            total_left += 1
    for no in right_nos:
        if no == key:
            total_right += 1
    sim_score += key * total_right * total_left 
    
    no_dict[key] = [total_left, total_right]

print(sim_score)


    