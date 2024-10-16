makan = input("sudah makan?: ")
mandi = input("sudah mandi?: ")
transportasi = input("pilih transportasi: ")
waktu = 0

if makan == "ya":
    waktu == 0
else : 
    waktu += 15

if mandi == "ya":
    waktu == 0
else : 
    waktu += 10
if transportasi == "motor":
    waktu += 15
else:
    waktu+=30
    print()
print(f"total waktu persiapan dan perjalanan:{waktu} menit")

if waktu > 60:
    print("kamu terlambat")
else : 
    print("kamu berangkat tepat waktu")


