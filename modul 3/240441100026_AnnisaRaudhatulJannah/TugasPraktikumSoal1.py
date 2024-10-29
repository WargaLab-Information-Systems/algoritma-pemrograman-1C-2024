size = int(input("Masukkan Size: "))

# Angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print('x' * size)
    else:
        print('x' + ' ' * (size - 2) + 'x')
 
print()  

# Angka 2
for i in range(size):
    if i == 0:  
        print('h' * size)
    elif i < size // 2:  
        print(' ' * (size - 1) + 'h')  
    elif i == size // 2:  
        print('h' * size)
    else: 
        print('h' + ' ' * (size - 1))  
    if i == size - 1:  
        print('h' * size)

print()  

# Angka 6
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print('x' * size)
    elif i < size // 2:
        print('x')
    else:
        print('x' + ' ' * (size - 2) + 'x')
