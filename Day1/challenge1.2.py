with open('input1.txt') as f:
    lines = f.readlines()
    res = 0
    nums = {'o':{'one':'1'},'t':{'two':'2','three':'3'},'f':{'four':'4','five':'5'},'s':{'six':'6','seven':'7'},'e':{'eight':'8'},'n':{'nine':'9'}}
    for line in lines:
        num = ""
        i = 0
        while (i < len(line)):
            ch = line[i]
            if ch in '0123456789':
                num += ch
            elif ch in nums:
                for n in nums[ch]:
                    if line[i:min(i+len(n),len(line))] == n:
                        num += nums[ch][n]
            i += 1
                
        if len(num)>1:
            new_num = num[0]+num[-1]
        else:
            new_num = num[0]+num[0]
        res+= int(new_num)
    print(res)