klub_basket = {
    "leader": "childe",
    "siswa": ["childe", "ayato", "alhaitham", "wriothesley", "diluc", "xiao", "kazuha", "kakavasha", "cyno", "kaeya", "thoma", "heizhou", "sethos"]
}

klub_renang = {
    "leader": "neuvilette",
    "siswa": ["neuvilette", "kaveh", "childe", "wriothesley", "freminet", "cyno", "scara", "kazuha", "dan heng", "kakavasha", "kaeya", "ga ming", "sethos"]
}

#a - 2 dictionary
print("Siswa yang mengikuti klub basket: ", klub_basket['siswa'])
print("Siswa yang mengikuti klub renang: ", klub_renang['siswa'])

# b - Siswa yang mengikuti kedua klub
siswa_kedua_klub = set(klub_basket["siswa"]).intersection(set(klub_renang["siswa"]))
print("Siswa yang mengikuti kedua klub: ", end="")
idx = 0
for nama in siswa_kedua_klub:
    if idx < len(siswa_kedua_klub) - 1:
        print(nama, end=", ")
    else:
        print(nama, end="")
    idx += 1
print()

# c - Siswa yang hanya mengikuti klub basket
hanya_basket = set(klub_basket["siswa"]).difference(set(klub_renang["siswa"]))
print("Siswa yang hanya mengikuti klub basket: ", end="")
idx = 0
for nama in hanya_basket:
    if idx < len(hanya_basket) - 1:
        print(nama, end=", ")
    else:
        print(nama, end="")
    idx += 1
print()

# Siswa yang hanya mengikuti klub renang
hanya_renang = set(klub_renang["siswa"]).difference(set(klub_basket["siswa"]))
print("Siswa yang hanya mengikuti klub renang: ", end="")
idx = 0
for nama in hanya_renang:
    if idx < len(hanya_renang) - 1:
        print(nama, end=", ")
    else:
        print(nama, end="")
    idx += 1
print()

# d - Semua siswa unik yang mengikuti setidaknya satu dari kedua klub
semua_siswa = set(klub_basket["siswa"]).union(set(klub_renang["siswa"]))
print("Semua siswa unik yang mengikuti setidaknya satu dari kedua klub: ", end="")
idx = 0
for nama in semua_siswa:
    if idx < len(semua_siswa) - 1:
        print(nama, end=", ")
    else:
        print(nama, end="")
    idx += 1
print()

# e - Jumlah semua siswa unik yang mengikuti setidaknya satu dari kedua klub
jumlah_siswa = len(semua_siswa)
print("Jumlah semua siswa unik yang mengikuti setidaknya satu dari kedua klub:", jumlah_siswa)
