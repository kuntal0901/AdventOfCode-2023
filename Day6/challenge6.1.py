with open('input6.txt') as f:
    lines = f.readlines()

    time,times = lines[0].split(":")
    distance,distances = lines[1].split(":")
    
    times = list(map(str,times.split()))
    distances = list(map(str,distances.split()))

    time = ''.join(times)
    distance = ''.join(distances)
    print(time,distance)
    ts,te = 0,0

    for t1 in range(int(time)+1):
        distnace_calc = t1*(int(time)-t1)
        if distnace_calc > int(distance):
            ts = t1
            break

    for t2 in range(int(time)+1,-1,-1):
        distnace_calc = t2*(int(time)-t2)
        if distnace_calc > int(distance):
            te = t2
            break
    print(ts,te)
    print(int(time)+1-ts-(int(time)+1-te))
