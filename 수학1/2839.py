N = int(input())
max = N // 5
count = 0
for i in range(max, -1,-1):
    r = N - 5 * i
    if r % 3 != 0:
        count = -1
    else:
        count = i + r // 3
        break
print(count)

