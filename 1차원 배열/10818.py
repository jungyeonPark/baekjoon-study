N = int(input())
data = [0] * N
data = list(map(int,input().split()))   #공백으로 구분한 정수를 입력받아 리스트로 만듦

min = data[0]
max = data[0]

for i in data:
    if i < min:
        min = i
    if i > max:
        max = i

print(min, max)