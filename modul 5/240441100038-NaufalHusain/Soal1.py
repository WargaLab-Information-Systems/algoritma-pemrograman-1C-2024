# Program menghitung diskon dan jenis keanggotaan pembeli
def calculate_discount(total_belanja, jenis_keanggotaan):
    diskon = 0

    # Diskon yang ditentukan berdasarkan jenis keanggotaan
    # lower untuk perbandingan jenis keanggotaan tidak sensitif terhadap huruf besar atau kecil
    if jenis_keanggotaan.lower() == "gold":
        diskon = 15
        print("Anda mendapatkan diskon 15%")
    elif jenis_keanggotaan.lower() == "silver":
        diskon = 10
        print("Anda mendapatkan diskon 10%")
    elif jenis_keanggotaan.lower() == "bronze":
        diskon = 5
        print("Anda mendapatkan diskon 5%")
    else:
        diskon = 0  # Tidak ada diskon jika tidak memiliki keanggotaan

    # Diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 5 

    # Menghitung total diskon
    total_diskon = (diskon / 100) * total_belanja
    total_setelah_diskon = total_belanja - total_diskon

    return total_diskon, total_setelah_diskon

def main():
    # Ambil input dari pengguna
    total_belanja = input("Masukkan total belanja: ")

    # Validasi input total belanja
    if total_belanja.replace('.', '', 1).isdigit() and float(total_belanja) >= 0:
        total_belanja = float(total_belanja)
    else:
        print("Total belanja tidak valid. Pastikan untuk memasukkan angka positif.")
        return

    # Validasi jenis keanggotaan
    while True:
        jenis_keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak Ada): ")
        if jenis_keanggotaan in ("gold", "silver", "bronze", "tidak ada"):
            break
        else:
            print("Input tidak valid. Silahkan ulangi lagi.")

    # Menghitung diskon dan total setelah diskon
    diskon, total_setelah_diskon = calculate_discount(total_belanja, jenis_keanggotaan)

    # Output hasil
    print(f"Total Diskon: {diskon:.2f}")
    print(f"Total Setelah Diskon: {total_setelah_diskon:.2f}")

main()