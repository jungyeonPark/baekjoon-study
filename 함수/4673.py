def d(n):
    s = str(n)
    ans = n
    for c in s:
        ans += int(c)
    return ans
        
if __name__ == "__main__":
    n = []
    ans = 0
    for i in range(1, 10001):
        ans = d(i)
        if ans <= 10000:
            n.append(ans)
    
    for i in range(1, 10001):
        if i not in n:
            print(i)