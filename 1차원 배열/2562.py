data_list = [0] * 9
max = 0
max_num = 0
for i in range(9):
    data = int(input())
    if data > max:
        max = data
        max_num = i + 1

print("{}\n{}".format(max, max_num))
    