w_makan = 15
w_mandi = 10
w_jalan = 30
w_motor = 15

waktu = 0

print("SEMANGAT NGAMPUSS!!")

print("Get Ready Now!")
print()
mandi = input("Apakah kamu sudah mandi? ")
if mandi == "tidak" :
    waktu = waktu + w_mandi
else :
    waktu += waktu

makan = input("Apakah kamu sudah makan? ")
if makan == "tidak" :
    waktu = waktu + w_makan
else :
    waktu += waktu

trans = input("Apa transportasi kamu untuk berangkat ke kampus? jalan/motor ")
if trans == "jalan" :
    waktu = waktu + w_jalan
elif trans == "motor":
    waktu = waktu + w_motor
else :
    print("Tolong pilih salah satu dari pilihan di atas!")
    waktu += waktu

print(f"Waktu yang kamu habiskan dalam persiapan dan perjalanan: {waktu} menit")

if waktu < 60 or waktu < 0:
    print("Kamu berangkat tepat waktu ><!")
else :
    print("Kamu terlambat..:(")