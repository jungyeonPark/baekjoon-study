r = []
for i in range(10):
    N = int(input()) % 42
    if N not in r:
        r.append(N)

print(len(r))