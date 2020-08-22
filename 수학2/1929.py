M, N = map(int, input().split())
num = [1 for x in range(0, 1000001)]
num[0] = 0
num[1] = 0
for i in range(2, 1001):
    n = i
    if num[i] == 1:
        while i * n <= 1000000:
            num[i * n] = 0
            n += 1

for i in range(M, N + 1):
    if num[i] == 1:
        print(i)
