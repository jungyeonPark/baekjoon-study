'''
혼자 힘으로 풀어 보기
data = list(map(int, input().split()))
flag = 0
for i in range(1, len(data)):
    if (flag == 0 or flag == "ascending") and data[i] > data[i - 1]:
        flag = "ascending"
    elif (flag == 0 or flag == "descending") and data[i] < data[i - 1]:
        flag = "descending"
    else:
        flag = "mixed"
        break

print(flag)
'''

a = list(map(int, input().split()))

ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i - 1]:
        descending = False
    elif a[i] < a[i - 1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')