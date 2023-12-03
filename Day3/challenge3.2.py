
def get_gear_positions(j,i):
    pos = [[0,-1],[-1,0],[1,0],[0,1],[1,1],[-1,-1],[1,-1],[-1,1]]
    res_pos = []
    for x,y in pos:
        if (j+x) in range(len(lines)) and (i+y) in range(len(lines[0])):
            if lines[j+x][i+y] == "*":
                res_pos.append([j+x,i+y])
    return res_pos
    

with open('input3.txt') as f:
    lines = f.readlines()

    res = 0
    d = [[[1,0]]*len(lines[0]) for _ in range(len(lines))]
    for j in range(len(lines)):
        line = lines[j]
        num = ""
        flag = []
        for i in range(len(line)):
            ch = line[i]
            
            if ch in '0123456789':
                num += ch
                flag.extend(get_gear_positions(j,i))
            else:
                visit = []
                for x in flag:
                    if x not in visit:
                        visit.append(x)
                if len(num) > 0 and len(visit) > 0:
                    for x,y in visit:
                        d[x][y] = [d[x][y][0]*int(num),d[x][y][1]+1] 
                    print(i,j,d[x][y])
                flag = []
                num = ""

    for i in range(len(d)):
        for j in range(len(d[0])):
            if d[i][j][1] == 2:
                res += d[i][j][0]


    print(res)


