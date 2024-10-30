makan = input("Sudah makan? ")
mandi = input("Sudah mandi? ")
tranportasi = input("Pilih transportasi 'motor' atau 'jalan kaki'? ")
waktu = 0
if makan == "ya":
    if mandi == "ya":
        while tranportasi == "jalan":
            waktu = 30
            if tranportasi == "motor":
                waktu = waktu + 15
        else:
            print("Input tidak diketahui silahkan masukkan lagi ")
    else:
        waktu = waktu + 10
else:
    waktu = waktu + 15


print(f"Total waktu persiapan dan perjalan {waktu} menit")
if waktu > 60:
    print("Kamu terlambat")
else:
    print("Kamu berangkat tepat waktu")





