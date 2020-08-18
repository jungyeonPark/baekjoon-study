S = input()
count = 0
for i in range(len(S)):
    if S[i] == " ":
        if i == 0 or i == len(S) - 1:
            continue
        elif S[i - 1] != " " and S[i + 1] != " ":
            count += 1
if S != " ":           # 주어진 문자열이 공백인 경우는 0이 나와야 함!!!!!!
    count += 1

print(count)
