import itertools
import operator
import copy
import time

start_time = time.time()



equations = []

with open('day7\\data7.txt', 'r') as f:
    for line in f.read().split('\n'):
        answer = int(line.split(': ')[0])
        nums = [int(num) for num in line.split(': ')[1].split(' ')]
        equations.append([answer, nums])

f.close()

def generate_equations(target,nums):    
    ops = { "+": operator.add, "*": operator.mul}
    correct = False
    total = 0
    
    n_symbols = len(nums)-1
    symbols = [x for x in itertools.product('*+', repeat=n_symbols)]

    
    for i in range(len(symbols)):
        if correct == True:
            break
        
        else:
        
            nums_copy = copy.deepcopy(nums)
        
            for j in range(len(nums_copy)-1):
            
                answer = ops [symbols[i][j]] (nums_copy[j],nums_copy[j+1])
                nums_copy[j+1] = answer
     
            if answer == target:
                correct = True
                total = answer
                break
        
    return total


total_sum = 0
count = 0

for line in equations:
    print('line:', count)
    count+= 1
    total_sum += generate_equations(line[0],line[1])

print(total_sum)

# correct : 538191549061