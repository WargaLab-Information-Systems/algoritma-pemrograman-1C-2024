#tugas membuat program denda keterlambatan pinjaman DVD
jawab="ya"

while (jawab == ("ya")):
    lama_pinjaman=int(input("berapa hari anda meminjam dvd:"))
    denda = 0
    if lama_pinjaman >5:
        for i in range(6,lama_pinjaman+1):
            denda+=2500
            if i % 5 == 0:
                denda+=5500
        print(f"anda terlambat mengembalikan dvd selama {lama_pinjaman} hari, anda harus membayar denda sebesar:",denda)
        jawaban =(input("ingin menghitung ulang? (ya/tidak?):"))
        if jawaban == "tidak":
            break
    else:
        print("anda tepat waktu")
        jawab=(input("ingin menghitung ulang? (ya/tidak?):"))
        if jawab != "tidak":
            break