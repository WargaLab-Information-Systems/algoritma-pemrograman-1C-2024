size = int(input("masukkan angka :"))

# membuat pola angka dengan menggunakan "x" membentuk pola angka "0"
rumus=int(size/2)
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2) + "x")
for i in range(1,rumus):  
    print("x"+" " * (size - 2) + "x") 
print("x" * size)

# membuat pola angka dengan menggunakan "x" membentuk pola angka "9"
rumus=int(size/2)
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2) + "x")
print("x" * size)
for i in range(1,rumus):
    print(""+" " * (size - 1) + "x")
print("x" * size)

# # membuat pola angka dengan menggunakan "x" membentuk pola angka "8"
rumus=int(size/2)
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2) + "x")
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2) + "x")
print("x" * size)

