def fibonacci(n):
    if n == 0:
        print("fibonacci(0) = 0")
        return 0
    elif n == 1:
        print("fibonacci(0) = 0")
        print("fibonacci(1) = 1")
        return 1
    else:
        print("fibonacci(0) = 0")
        print("fibonacci(1) = 1")
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
            print(f"fibonacci({i}) = {a} + {b - a} = {b}")
        return b

n = int(input("Masukkan Nilai n: "))
print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")
