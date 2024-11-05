while True:
  lama_sewa = int(input("Berapa hari lama penyewaan DVD Anda: "))

  if lama_sewa > 5:
    keterlambatan = lama_sewa - 5
    denda = keterlambatan * 2500
    if keterlambatan > 10:
      denda_tambahan = ((keterlambatan- 10) // 5) * 5500
      denda += denda_tambahan
    print("Total denda keterlambatan: Rp", denda)
  else:
    print("DVD dikembalikan tepat waktu, tidak ada denda.")

  hitung_lagi = input("Apakah Anda ingin menghitung lagi? (iya/tidak): ")
  if hitung_lagi != "iya":
    print("Terima kasih telah menyewa DVD di toko kami.")
    break