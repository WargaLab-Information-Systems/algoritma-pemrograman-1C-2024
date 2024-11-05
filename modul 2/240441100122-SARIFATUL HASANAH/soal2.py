# jaka
nama_jaka = input("Masukkan nama: ")
jaka_skor = int(input("Masukkan Nilai skor : "))
jaka_ipk = float(input("Masukkan ipk : "))

if jaka_skor > 1100 and jaka_ipk >= 3.0 :
    print(f"Selamat {nama_jaka}, anda lulus persyaratan beasiswa dengan skor sebanyak {jaka_skor} dan IPK sebanyak {jaka_ipk}")
elif jaka_skor <= 0 and jaka_ipk <= 0 :
    print("Nilai Yang anda masukkan salah")
else :
    print(f"Maaf {nama_jaka}, anda tidak lolos!!!")

# ida
nama_ida = "Ida"
ida_skor = 1000
ida_ipk = 3.5

if ida_skor > 1100 and ida_ipk >= 3.0 :
    print(f"Selamat {nama_ida}, anda lulus persyaratan beasiswa dengan skor sebanyak {ida_skor} dan IPK sebanyak {ida_ipk}")
else :
    print(f"Maaf {nama_ida}, anda tidak lolos!!!")

