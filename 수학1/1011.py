T = int(input())
data = []
for i in range(T):
    x, y = map(int, input().split())
    data.append(y - x)

for a in data:
    i = 0       # 지금 이동할 거리
    d = 0       # 현재까지 총 간 거리
    num = 0     # 이동한 횟수
    temp = 0    # 양쪽 같은 숫자를 계속 더하다가 못 더할때 남은 수 
    while True:
        if d == a:
            break
        elif d > a:  
            temp = a - (d - 2 * i)  
            num -= 2
            num += temp // i    # num은 0이나 1이 된다
            if temp % i != 0:   # 나머지가 있으면 1 더함
                num += 1
            break
        else:       # i를 증가시키면서 양쪽 끝에 같은 거리를 추가
            i += 1
            d += i * 2
            num += 2
    print(num)

'''
0 ~ 3
1 1 1

1 ~ 5
1 2 1 

45 ~ 50
1 2 1 1
'''