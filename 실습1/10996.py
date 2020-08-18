N = int(input())

if N == 1:      #is랑 ==차이 잘 알아둘 것
    print("*")
else:
    n = N // 2
    if N % 2 != 0:  #올림
        n += 1
    for i in range(N):
        for j in range(n):
            print("*", end=" ")
        print("")

        if N % 2 == 0:
            for j in range(n):
                print(" *", end="")
        else:
            for j in range(n - 1):
                print(" *", end="")
        print("")


