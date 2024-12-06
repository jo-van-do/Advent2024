with open('day4\data4.txt', 'r') as f:
    txt = f.read().split('\n')
f.close()
   
    
def diag_xmas(text, i, j):
    n_xmas = 0

    left = text[i-1][j-1] + text[i+1][j+1]
    right = text[i-1][j+1] + text[i+1][j-1]
    
    if left == 'MS' or left == 'SM':
        if right == 'MS' or right == 'SM':
            n_xmas = 1
        
    return n_xmas
    
    
total = 0

for i, line in enumerate(txt):
    for j, char in enumerate(line):
        if char == 'A' and 0 < i < (len(txt)-1) and 0 < j < (len(line)-1):
            total += diag_xmas(txt,i,j)

print(total)
    
