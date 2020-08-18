A = int(input())
B = int(input())
C = int(input())
num = A * B * C
count = [0] * 10

while num != 0:
    r = num % 10 
    for j in range(10):
        if r == j:
            count[j] += 1
            break
    num = num // 10

for i in range(10):
    print(count[i])