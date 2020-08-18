T = int(input())
num = [[x+1 for x in range(15)]]
for i in range(1, 15): 
    a = []
    s = 0
    for j in range(1, 15):  
        s += num[i - 1][j - 1]
        a.append(s)
    num.append(a) 

for i in range(T):
    k = int(input())
    n = int(input()) - 1
    print(num[k][n])
