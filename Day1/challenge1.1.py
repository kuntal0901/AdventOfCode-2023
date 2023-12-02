with open('input1.txt') as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        num = ""
        for ch in line:
            if ch in '0123456789':
                num += ch
        if len(num)>1:
            new_num = num[0]+num[-1]
        else:
            new_num = num[0]+num[0]
        res+= int(new_num)
    print(res)