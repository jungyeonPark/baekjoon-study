S = input()
num = []
for i in S:
    n = ord(i) - 65
    if n <= 17:     # R까지
        num.append(n // 3 + 2)
    else:
        n -= 18     # S부터 0으로 다시 시작
        if n == 0:
            num.append(7)
        elif n // 4 == 0:
            num.append(8)
        else:
            num.append(9)
result = 0
for i in num:
    result += (i + 1)

print(result) 


