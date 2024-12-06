# Fungsi untuk menambah data siswa
def tambah_siswa():
   kelas = int(input("Masukkan nomor kelas: "))
   
   # Hitung jumlah siswa di kelas tersebut
   siswa_di_kelas = sum(1 for siswa in data_siswa if siswa['kelas'] == kelas)
   
   if siswa_di_kelas >= 3:
       print(f"Maaf, kelas {kelas} sudah penuh (maksimal 3 siswa).")
       return
       
   nama = input("Masukkan nama siswa: ")
   asal_sekolah = input("Masukkan asal sekolah: ")
   bimbingan = input("Masukkan bidang bimbingan: ")
   data_siswa.append({'nama': nama, 'kelas': kelas, 'asal_sekolah': asal_sekolah, 'bimbingan': bimbingan})
   print(f"Data siswa {nama} berhasil ditambahkan ke kelas {kelas}")

# Fungsi untuk menampilkan data siswa
def tampilkan_data():
   print("\nData Siswa Bimbingan Intensif:")
   for siswa in data_siswa:
       print(f"Nama: {siswa['nama']}, Kelas: {siswa['kelas']}, Asal Sekolah: {siswa['asal_sekolah']}, Bimbingan: {siswa['bimbingan']}")

# Fungsi untuk menghapus data siswa
def hapus_siswa():
   nama = input("Masukkan nama siswa yang ingin dihapus: ")
   for i, siswa in enumerate(data_siswa):
       if siswa['nama'] == nama:
           del data_siswa[i]
           print(f"Data siswa {nama} berhasil dihapus.")
           return
   print(f"Siswa dengan nama {nama} tidak ditemukan.")

# Fungsi untuk mengubah data siswa
def ubah_data():
   nama = input("Masukkan nama siswa yang ingin diubah: ")
   for siswa in data_siswa:
       if siswa['nama'] == nama:
           new_kelas = int(input(f"Masukkan nomor kelas baru untuk {nama}: "))
           
           # Hitung jumlah siswa di kelas baru (tidak termasuk siswa yang diubah)
           siswa_di_kelas_baru = sum(1 for s in data_siswa if s['kelas'] == new_kelas and s['nama'] != nama)
           
           if siswa_di_kelas_baru >= 3:
               print(f"Maaf, kelas {new_kelas} sudah penuh (maksimal 3 siswa).")
               return
               
           siswa['kelas'] = new_kelas
           siswa['asal_sekolah'] = input(f"Masukkan asal sekolah baru untuk {nama}: ")
           siswa['bimbingan'] = input(f"Masukkan bidang bimbingan baru untuk {nama}: ")
           print(f"Data siswa {nama} berhasil diubah.")
           return
   print(f"Siswa dengan nama {nama} tidak ditemukan.")

# Data siswa
data_siswa = []

# Menu utama
while True:
   print("\nMenu:")
   print("1. Tambah Data Siswa")
   print("2. Tampilkan Data Siswa")
   print("3. Hapus Data Siswa")
   print("4. Ubah Data Siswa")
   print("5. Keluar")
   
   pilihan = input("Masukkan pilihan (1-5): ")
   
   if pilihan == '1':
       tambah_siswa()
   elif pilihan == '2':
       tampilkan_data()
   elif pilihan == '3':
       hapus_siswa()
   elif pilihan == '4':
       ubah_data()
   elif pilihan == '5':
       print("Terima kasih telah menggunakan program ini.")
       break
   else:
       print("Pilihan tidak valid. Silakan coba lagi.")
