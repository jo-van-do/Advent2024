
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

muls = re.findall("mul[(]\d{1,3},\d{1,3}[)]", txt)

print(add_muls(muls))


