S = input()
d = {}
for i in range(len(S)):
    if S[i] in d.keys():
        continue
    else:
        d[S[i]] = i

a = "abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i in d.keys():
        print(d[i], end = " ")
    else:
        print(-1, end = " ")
       