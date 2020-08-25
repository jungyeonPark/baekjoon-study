import math
num = [1 for x in range(0, 10000 + 1)]
num[0] = 0
num[1] = 0
for i in range(2, int(math.sqrt(10000)) + 1): 
    if num[i] == 1:
        j = i
        while i * j <= 10000:
            num[i * j] = 0
            j += 1

T = int(input())
for i in range(T):
    n = int(input())
    partition = [0] * 2
    for j in range(2, n // 2 + 1): 
        if num[j] == 0:
            continue
        else:
            if num[n - j] == 0:
                continue
            else:
                if partition[0] == 0 or partition[1] - partition[0] > n - j - j:
                    partition[0] = j
                    partition[1] = n - j

    print("{} {}".format(partition[0], partition[1]))
