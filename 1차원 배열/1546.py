N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
rescore = [(data / max_score) * 100 for data in score]
avg = 0
for data in rescore:
    avg += data
avg = avg / N
print(avg)