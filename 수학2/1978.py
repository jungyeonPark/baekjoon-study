import math
N = int(input())
data = list(map(int, input().split()))
count = 0
for d in data:
    if d == 1:
        continue
    elif d == 2:
        count += 1
        continue
    r = int(math.sqrt(d)) + 1   # 에라토스테네스의 체에서 봄
    for i in range(2, r + 1):
        if i == r:         # 플래그를 쓰는 방법도 있다
            count += 1
        if d % i == 0:
            break
print(count)