s = input().lower()
d = {}
for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

max_value = 0
equal_key = ""
for i in d.keys():
    if d[i] > max_value:
        max_value = d[i]
        max_key = i
    elif d[i] == max_value:
        equal_key = i

if equal_key != "":
    if d[equal_key] == d[max_key]:
        print("?")
    else:
        print(max_key.upper())
else:
    print(max_key.upper())

