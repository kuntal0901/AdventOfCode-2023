with open('input2.txt') as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        game,inputs = line.split(":")
        game =game.replace("Game","")
        configs = inputs.split(";")
        r,g,b = 0,0,0
        for conf in configs:
            colors_count = conf.split(",")
            for color_count in colors_count:
                if "red" in color_count:
                    color_count = color_count.replace("red","")
                    r = max(r,int(color_count))
                if "blue" in color_count:
                    color_count = color_count.replace("blue","")
                    b = max(b,int(color_count))
                if "green" in color_count:
                    color_count = color_count.replace("green","")
                    g = max(g,int(color_count))
        if r<=12 and g<=13 and b<=14:
            res += int(game)
    print(res)