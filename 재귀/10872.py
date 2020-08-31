def factorial(n):
    if n - 1 > 0:
        n *= factorial(n-1)
    return n

if __name__ == '__main__':
    N = int(input())
    if N == 0:      # 0팩토리얼은 1이다 !!
        print(1)
    else:
        print(factorial(N))