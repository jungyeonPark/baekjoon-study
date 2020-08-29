import math
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    length = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if r1 + r2 == length:  
        print(1)
        continue
    elif r1 + r2 < length:
        print(0)
        continue
    else:
        if x1 == x2 and y1 == y2:   
            if r1 == r2:    
                print(-1)
                continue
            else:               # 중심이 같고 반지름이 다를 때
                print(0)
                continue
        elif r1 == length + r2 or r2 == length + r1:  # 큰 원 안에서 작은 원이 접하면
            print(1)
            continue
        elif r1 > length + r2 or r2 > length + r1:     # 큰 원 안에 작은 원이 있으면
            print(0)
            continue
        else:
            print(2)
            continue    