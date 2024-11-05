while True:
    try:
        maksimal = 60
        waktu = 0
        makan = str(input("Sudah makan? "))
        mandi = str(input("Sudah mandi? "))
        transportasi = str(input("Pilih transportasi: "))
        if makan == "ya":
            waktu += 0
        else:
            waktu += 15
        if mandi == "ya":
            waktu += 0
        else:
            waktu += 10
        if transportasi == "motor":
            waktu += 15
        elif transportasi == "jalan kaki":
            waktu += 30
        else:
            print("Input tidak valid")
            break
        print(f"Total waktu persiapan dan perjalanan: {waktu} menit")
        if waktu > maksimal:
            print("Kamu terlambat")
        else:
            print("Kamu berangkat tepat waktu")
        break
    except ValueError:
        print("Masukkan inputan yang benar")