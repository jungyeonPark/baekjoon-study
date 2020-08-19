
'''
1 2 3 4 5 6 ...
1 3 6 10 15 21 ...
1 4 10 20 35 56 ... 
'''
T = int(input())
num = [[x for x in range(1, 15)]]
for i in range(1, 15): 
    a = []
    s = 1
    a.append(s)
    for j in range(1, 14):  
        s += num[i - 1][j]
        a.append(s)
    num.append(a)

for i in range(T):
    k = int(input())
    n = int(input()) - 1
    print(num[k][n])

