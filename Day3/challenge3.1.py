import re

def is_special_character(char):
    return bool(re.match(r'[^a-zA-Z0-9.]', char))


def is_special_adj(j,i):
    pos = [[0,-1],[-1,0],[1,0],[0,1],[1,1],[-1,-1],[1,-1],[-1,1]]
    for x,y in pos:
        if (j+x) in range(len(lines)) and (i+y) in range(len(lines[0])):
            if is_special_character(lines[j+x][i+y]) and lines[j+x][i+y] !='\n':
                return True
    return False
    

with open('input3.txt') as f:
    lines = f.readlines()

    res = 0
    for j in range(len(lines)):
        line = lines[j]
        num = ""
        flag = False
        for i in range(len(line)):
            ch = line[i]
            
            if ch in '0123456789':
                num += ch
                flag = flag or is_special_adj(j,i)
            else:
                if len(num)>0 and flag:
                    res += int(num)
                flag = False
                num = ""
    print(res)


