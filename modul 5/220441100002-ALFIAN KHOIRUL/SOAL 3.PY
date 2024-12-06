def factorial(n):
    # Kasus dasar: faktorial dari 0 adalah 1
    if n == 0:
        return 1
    
    # Inisialisasi hasil
    result = 1
    
    # Menghitung faktorial dengan mengalikan angka dari 1 sampai n
    for i in range(1, n + 1):
        result *= i
    
    return result

# Contoh penggunaan
print("5! =", factorial(5))  # Akan menghasilkan: 5! = 120
print("3! =", factorial(3))  # Akan menghasilkan: 3! = 6
print("2! =", factorial(2))  # Akan menghasilkan: 2! = 2
print("0! =", factorial(0))  # Akan menghasilkan: 0! = 1