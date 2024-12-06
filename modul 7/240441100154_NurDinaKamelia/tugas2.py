def analisis_klub(siswa_basket, siswa_renang):
  # Siswa yang mengikuti kedua klub
  kedua_klub = siswa_basket.intersection(siswa_renang)

  # Siswa yang hanya mengikuti satu klub
  hanya_satu_klub = (siswa_basket | siswa_renang)

  # Semua siswa unik
  semua_siswa = siswa_basket | siswa_renang

  print("Siswa yang mengikuti kedua klub:", kedua_klub)
  print("Siswa yang hanya mengikuti satu klub:", hanya_satu_klub)
  print("Semua siswa unik:", semua_siswa)
  print("Jumlah siswa unik:", len(semua_siswa))

# data siswa klub
siswa_basket = {"Andi", "Budi", "Cici", "Dedi", "Efi"}
siswa_renang = {"Budi", "Cici", "Fatimah", "Gani"}

analisis_klub(siswa_basket, siswa_renang)