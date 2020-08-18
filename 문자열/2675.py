T = int(input())
for i in range(T):
    R, S = input().split()
    result = ''
    for i in range(len(S)):
        result += S[i] * int(R) # 문자열에 곱하기 가능!!!
    print(result)

# 딕셔너리를 사용하면 안되는 이유
# : 중복되는 문자가 들어오면 한개만 출력되기 때문 !!!
