M = int(input())
N = int(input())
num = [1 for x in range(0, 10001)]
num[0] = 0
num[1] = 0
for i in range(2, 101):
    n = i
    if num[i] == 1:
        while i * n <= 10000:
            num[i * n] = 0
            n += 1
sum = 0
min = 0
for i in range(M, N + 1):
    if num[i] == 1:
        sum += i
        if min == 0:
            min = i
if sum > 0:
    print("{}\n{}".format(sum, min))
else:
    print(-1)