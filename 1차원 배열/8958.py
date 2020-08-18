N = int(input())
result = []
for i in range(N):
    ox = input()
    score = []
    for i in range(len(ox)):
        if ox[i] == 'O':
            if i == 0:
                score.append(1)
            else:
                if score[i-1] > 0:
                    score.append(score[i-1] + 1)
                else:
                    score.append(1)
        else:
            score.append(0)
    score_sum = 0
    for data in score:
        score_sum += data
    result.append(score_sum)

for data in result:
    print(data)
