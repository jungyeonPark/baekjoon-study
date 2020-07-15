score = [0 for i in range(5)]
for i in range(5):
    score[i] = int(input())
    if score[i]<40:
        score[i] = 40

avg= sum(score)/5
print(int(avg))




