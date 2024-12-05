
import string

rules = []
pages = []
middle_nums = []

def is_bigger(page1, page2):
    if "{0}>{1}".format(page1, page2) in rules:
        return True
    else:
        return False
    
def get_middle(alist):
    middle = int((len(alist) - 1)/2)
  
    return alist[middle]


with open('day5\data5.txt', 'r') as f:
    for line in f.read().split('\n'):
        if '|' in line:
            rules.append('{}>{}'.format(line.split('|')[1],line.split('|')[0]))
        else:
            pages.append(line)
f.close()


for pageline in pages[1:]:
    pageline = pageline.split(',')
    condition = True
    
    for i, num in enumerate(pageline):
        for j in range(i+1,len(pageline)):
            if is_bigger(num,pageline[j]):
                condition = False
                break
            break
    
    if condition:
        middle_nums.append(int(get_middle(pageline)))

print(sum(middle_nums))

    


