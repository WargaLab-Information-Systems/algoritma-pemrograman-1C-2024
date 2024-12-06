n = int(input("Masukkan bilangan bulat : "))

def fibonacci(n):
    # Basis kasus: jika n adalah 0 atau 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
if n < 0:
    print("Masukkan bilangan bulat!")
else:
    print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")

