with open('day4\data4.txt', 'r') as f:
    txt = f.read().split('\n')
f.close()



def hori_xmas(text, i, j):
    n_xmas = 0
    
    if j < (len(text[i])-3):
        mask = text[i][j+1] + text[i][j+2] + text[i][j+3]
        if mask == 'MAS':
            n_xmas += 1
    if j > 2:
        mask = text[i][j-1] + text[i][j-2] + text[i][j-3]
        if mask == 'MAS':
            n_xmas += 1
    
    return n_xmas

def verti_xmas(text,i,j):
    n_xmas = 0
    upper = ''
    lower = ''
    
    if i < (len(text) - 3):
        for id in range(1,4):
            lower += text[i+id][j]
        if lower == 'MAS':
            n_xmas += 1
    if i > 2:
        for id in range(1,4):
            upper += text[i-id][j]
        if upper == 'MAS':
            n_xmas += 1
    
    return n_xmas
    
    
def check_lowerright(text, i, j):
    n_xmas = 0

    mask = text[i+1][j+1] + text[i+2][j+2] + text[i+3][j+3]
    if mask == 'MAS':
        n_xmas = 1
        
    return n_xmas

def check_lowerleft(text, i, j):
    n_xmas = 0

    mask = text[i+1][j-1] + text[i+2][j-2] + text[i+3][j-3]
    if mask == 'MAS':
        n_xmas = 1
        
    return n_xmas

def check_upperleft(text, i, j):
    n_xmas = 0

    mask = text[i-1][j-1] + text[i-2][j-2] + text[i-3][j-3]
    if mask == 'MAS':
        n_xmas = 1
        
    return n_xmas

def check_upperright(text, i, j):
    n_xmas = 0

    mask = text[i-1][j+1] + text[i-2][j+2] + text[i-3][j+3]
    if mask == 'MAS':
        n_xmas = 1
        
    return n_xmas
    

def diag_xmas(text,i,j):
    n_xmas = 0
    
    if i < (len(text) - 3) and j < (len(text[i])-3):
        n_xmas += check_lowerright(text,i,j)

    if i < (len(text) - 3) and j > 2:
        n_xmas += check_lowerleft(text,i,j)

    if i > 2 and j > 2:
        n_xmas += check_upperleft(text,i,j)

    if i > 2 and j < (len(text[i]) -3):
        n_xmas += check_upperright(text,i,j)
    
    return n_xmas
    

def check_xmas(text, i, j):
    total_xmas = 0
    total_xmas = hori_xmas(text, i, j) + verti_xmas(text, i, j) + diag_xmas(text, i, j)
        
    return total_xmas
    
total = 0

for i, line in enumerate(txt):
    for j, char in enumerate(line):
        if char == 'X':
            total += check_xmas(txt,i,j)

print(total)
    
