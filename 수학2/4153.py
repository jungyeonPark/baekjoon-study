t = [1] * 3
while t[0] != 0 and t[1] != 0 and t[2] != 0:
    t = list(map(int, input().split()))
    if t[0] > t[1] and t[0] > t[2]:
        if t[0] ** 2 == t[1] ** 2 + t[2] ** 2:
            print("right")
        else:
            print("wrong")
    if t[1] > t[0] and t[1] > t[2]:
        if t[1] ** 2 == t[0] ** 2 + t[2] ** 2:
            print("right")
        else:
            print("wrong")
    if t[2] > t[1] and t[2] > t[0]:
        if t[2] ** 2 == t[1] ** 2 + t[0] ** 2:
            print("right")
        else:
            print("wrong")
    

