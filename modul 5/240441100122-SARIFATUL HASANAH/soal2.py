def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True :
    n = int(input("Masukkan bilangan bulat yang ingin dicari Fibonacci-nya : "))

    if n < 0:
        print("Silakan masukkan bilangan bulat non-negatif.")
    else:
        print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")
        break

# 0 1 1 2 3 5 8 13 21
