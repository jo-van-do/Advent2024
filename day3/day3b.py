
import re

with open('day3\data3.txt', 'r') as f:
    txt = f.read()
f.close()

def mul_mul(mul):
    """multiplies x and y if input is correct
    """
    nums = re.findall('\d{1,3}', mul)
    x = int(nums[0])
    y = int(nums[1])

    return x * y

def add_muls(mullist):
    total = 0 
    
    for mul in mullist:
        mul = mul_mul(mul)
        total += mul
        
    return total

def create_indices(idx1,idx2):
    indices = []
    idx1[0] = 0 
    stop = 0
        
    for id1 in idx1:
        start = id1
        if id1 < stop:
            continue
        for id2 in idx2:
            if id2 > id1:
                stop = id2
                indices.append(slice(start,stop))
                break
    
    indices.append(slice(idx1[-1],-1)) # oops hardcoded failsafe :$
            
    return indices


dos = [i for i in range(len(txt)) if txt.startswith('do()', i)]
donts = [i for i in range(len(txt)) if txt.startswith("don't()", i)]

newtext = ''
for sls in create_indices(dos, donts):
    newtext += (txt[sls])

muls = re.findall("mul[(]\d{1,3},\d{1,3}[)]", newtext)
print(add_muls(muls))
