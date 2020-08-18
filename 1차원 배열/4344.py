C = int(input())
result = []
for i in range(C):
    score = list(map(int, input().split()))
    avg = 0
    for i in range(1, score[0] + 1):
        avg += score[i]
    avg = avg / score[0]
    
    n = 0
    for i in range(1, score[0] + 1):
        if score[i] > avg:
            n += 1
            
    result.append(n / score[0])

for i in range(len(result)):
    print(format(result[i], "0.3%"))