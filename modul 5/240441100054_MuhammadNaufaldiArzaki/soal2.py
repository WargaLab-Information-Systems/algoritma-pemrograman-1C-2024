def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        print("Harap masukkan angka positif!")

while True:
        n = int(input("Masukkan angka positif: "))
        if n < 0:
            print("Harap masukkan angka positif!!")
            continue
        break
else:
     print("Input tidak valid, harap masukkan angka.")
    
print(f"Bilangan Fibonacci ke-{n} adalah: {fibonacci(n)}")