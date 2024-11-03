n = int(input("fibonacci ke "))

def fibonacci(n):
    # Memeriksa kasus dasar
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Menggunakan rekursi untuk menghitung nilai Fibonacci
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(f"Fibonacci ke-{n} adalah {fibonacci(n)}") 

