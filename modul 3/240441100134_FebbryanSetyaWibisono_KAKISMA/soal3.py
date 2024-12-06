while True:
    try:
        lama_pinjam = int(input("Berapa lama anda meminjam DVD?(hari): "))
        batas_pinjam = 5
        denda = 2500
        denda_tambahan = 5500
        batas_terlambat = lama_pinjam - batas_pinjam
        total_denda = 0
        if lama_pinjam > 5:
            total_denda = batas_terlambat * denda
            if batas_terlambat > 10:
                total_denda += ((batas_terlambat - 5) // 5) * denda_tambahan
        print(f"Total denda anda adalah Rp. {total_denda}")
        hitung_lagi = str(input("Apakah anda ingin menghitung lagi?(ya?tidak): "))
        if hitung_lagi != "ya":
            break
    except ValueError:
        print("Input tidak valid. Mohon untuk menginputkan bilangan bulat")