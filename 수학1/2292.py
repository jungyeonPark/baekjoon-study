'''
1 -> ~1
2 -> ~7(6)
3 -> ~19(12)
4 -> ~37(18)
5 -> ~61(24)
'''
N = int(input())
a = 1
b = 1
if N == 1:
    print(1)
else:
    while N > a:
        a += 6 * b
        b += 1
        # print(a)
    print(b)
