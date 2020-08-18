def find_groupWord(s : str) -> int:
    d = {}
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]] = i
        else:
            if d[s[i]] + 1 == i:
                d[s[i]] = i
            else:
                return 0
    return 1

if __name__ == "__main__":
    N = int(input())
    count = 0
    for i in range(N):
        S = input()
        count += find_groupWord(S)

    print(count)