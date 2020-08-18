i1, i2 = input().split()
n1 = ''.join(reversed(i1))      # "".join(list) : 리스트에서 문자열로 변환
n2 = ''.join(reversed(i2))
if int(n1) > int(n2):
    print(int(n1))
else:
    print(int(n2))
