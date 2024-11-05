n = int(input("masukkan nilai n:"))

def faktorial(n):
    # Basis kasus: jika n adalah 0 atau 1
    if n <= 1:
        return 1
    # Panggilan rekursif untuk menghitung faktorial
    else:
        return n * faktorial(n - 1)
print(f"n! = {faktorial(n)}")


# # Contoh penggunaan fungsi
# print(f"5! = {faktorial(5)}")
# print(f"3! = {faktorial(3)}")
# print(f"2! = {faktorial(2)}")
# print(f"0! = {faktorial(0)}")