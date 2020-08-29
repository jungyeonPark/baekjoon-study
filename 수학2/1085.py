# 직사각형은 경계선까지의 거리를 고려해서 대각선이 최소인 경우가 없으므로
# 대각선은 고려하지 않는다
# 출처: https://hwiyong.tistory.com/222

x, y, w, h = list(map(int, input().split()))
print(min([x, y, w - x, h - y]))

'''
import math
x, y, w, h = map(int, input().split())
min = math.sqrt(1000 * 1000) + 1
for i in range(2):
    a = 0
    if i == 1:
        a = w 
    for j in range(h + 1):
        if min > math.sqrt((x - a) ** 2 + (y - j) ** 2):
            min = math.sqrt((x - a) ** 2 + (y - j) ** 2)
for i in range(2):
    b = 0
    if i == 1:
        b = h
    for j in range(w + 1):
        if min > math.sqrt((x - j) ** 2 + (y - b) ** 2):
            min = math.sqrt((x - j) ** 2 + (y - b) ** 2)

print(round(min))
'''

  
