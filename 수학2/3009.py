def findCoordinate(arr):
    if arr[0] == arr[1]:
        return arr[2]
    elif arr[1] == arr[2]:
        return arr[0]
    else:
        return arr[1]

x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

print(findCoordinate(x), findCoordinate(y))

