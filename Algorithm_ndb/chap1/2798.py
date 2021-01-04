N, M = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i + 1, N):   # i + 1부터 해도 다 돔
        for k in range(j + 1, N):   # 마찬가지
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= M:
                result = max(result, sum_value)    # 둘 중에 큰거
print(result)
            