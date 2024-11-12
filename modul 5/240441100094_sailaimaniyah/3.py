def factorial(n):
    if n == 0:
        return 1
    else:
        # Rekurens: n! = n * (n-1)!
        return n * factorial(n - 1)
    
n = int(input("Masukkan nilai n: "))
print(n,"!=",factorial(n))