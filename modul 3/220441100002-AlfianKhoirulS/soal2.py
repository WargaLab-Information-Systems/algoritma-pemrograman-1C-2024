while True:
    print("\n=== Program Membalikkan Angka ===")
    
    angka = input("Masukkan angka bulat: ")

    # Validasi input hanya berupa angka bulat positif
    if angka.isdigit():
        angka = int(angka)
        balik = 0

        # Loop untuk membalik angka
        while angka > 0:
            balik = (balik * 10) + (angka % 10)
            angka = angka // 10  # Pembagian bulat

        print(f"Angka setelah dibalik: {balik}")
    else:
        print("Input tidak valid. Masukkan angka bulat positif!")
    
    # Menanyakan apakah ingin mengulang
    ulang = input("\nApakah Anda ingin mencoba lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih telah menggunakan program!")
        break
