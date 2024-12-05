
import string

rules = []
pages = []
middle_nums = []
incorrects = []


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
   
    for i, num in enumerate(pageline):
        for j in range(i+1,len(pageline)):
            if is_bigger(num,pageline[j]):
                if pageline not in incorrects:
                    incorrects.append(pageline)
                break
            break


for pageline in incorrects:
  
    for i, num in enumerate(pageline):
        for j in range(i+1,len(pageline)):
            while is_bigger(pageline[i],pageline[j]):
                pageline[i], pageline[j] = pageline[j], pageline[i]
                
    middle_nums.append(int(get_middle(pageline)))

print(sum(middle_nums))


