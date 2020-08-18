import math
T = int(input())
data =[]
for i in range(T):
    data.append(list(map(int, input().split())))

for i in range(T):
    floor = data[i][2] % data[i][0]
    if floor == 0:
        floor = data[i][0]
    room = math.ceil(data[i][2] / data[i][0])
    if room < 10:    
        print("{}0{}".format(floor, room))
    else:
        print("{}{}".format(floor, room))
