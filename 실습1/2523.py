N = int(input())

for i in range(2 * N - 1):
    if i + 1 > N:
        star_num_line = N - (i + 1 - N)
    else:
        star_num_line = i + 1
    for j in range(star_num_line):
        print("*", end="")

    if i is not 2 * N - 1 - 1:
        print("")
