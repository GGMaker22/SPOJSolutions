a = int(input())
T = "TAK"
N = "NIE"
I = 1


if a <= 1:
    print(N)
    quit()
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            print(N)
            quit()
print(T)
quit()