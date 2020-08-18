import math
X = int(input())
n = math.ceil((-1 +  math.sqrt(1 - 4 * (-2 * X))) / 2)    # 근의 공식
son = 0
mom = 0
r = X - n * (n - 1) / 2
if n % 2 == 0:
    mom = n - (r - 1)
    son = 1 + (r - 1)
else:
    son = n - (r - 1)
    mom = 1 + (r - 1)

print("{}/{}".format(int(son), int(mom)))
