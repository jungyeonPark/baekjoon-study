import math
num = [1 for x in range(0, 123456 * 2 + 1)]
num[0] = 0
num[1] = 0
for i in range(2, int(math.sqrt(123456 * 2)) + 1): 
    if num[i] == 1:
        j = i
        while i * j <= 123456 * 2:
            num[i * j] = 0
            j += 1

while True :
    n = 0
    count = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n + 1, 2 * n + 1):
        if num[i] == 1:
            count += 1
    print(count)
