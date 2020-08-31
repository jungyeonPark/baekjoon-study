MAX = 20
def fibonacci(fibo, n):
    if n <= MAX:
        fibo.append(fibo[n - 2] + fibo[n - 1])
        fibonacci(fibo, n + 1)

if __name__ == "__main__":
    N = int(input())
    fibo = [0, 1]
    fibonacci(fibo, 2)
    print(fibo[N])
    