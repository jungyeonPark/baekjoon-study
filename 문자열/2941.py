S = input()
count = 0
for i in range(len(S)):
    if i != 0:
        if S[i] == "=":
            if i > 1 and S[i-2:i] == "dz":
                count -= 1
                continue
            else:
                continue
        elif S[i] == "-":
            continue
        elif S[i] == "j":
            if S[i-1] == "l" or S[i-1] == "n":
                continue
    count += 1

print(count)
