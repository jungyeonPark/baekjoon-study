def f(n):
    count = 0
    for i in range(1, n + 1):
        if len(str(i)) < 3:
            count += 1
        else:
            s = str(i)
            d = int(s[1]) - int(s[0])
            if int(s[2]) - int(s[1]) == d:
                count += 1
    return count

if __name__ == "__main__":
    N = int(input())
    print(f(N))