N = int(input("Masukkan ukuran sisi belah ketupat (bilangan bulat positif): "))

for i in range(N):
    print(' ' * (N - i - 1), end='')
    print('*' * (2 * i + 1))

for j in range(N - 2, -1, -1):
    print(' ' * (N - j - 1), end='')
    print('*' * (2 * j + 1))