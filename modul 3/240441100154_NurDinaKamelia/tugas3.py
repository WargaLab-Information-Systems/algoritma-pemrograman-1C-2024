# # #(perulangan tak terbatas)

# # while True:
# # #meminta pengguna untuk memasukkan lama penyewaan
# #     hari_penyewaan = int(input("masukkan jumlah hari pemimjaman:"))
# #     hari_terlambat = int(input("masukkan jumlah hari keterlambatan:"))
# # #denda per hari keterlambatan
# #     denda_per_hari = 2500
# # #denda tambahan jika keterlambatan lebih dari 10 hari
# #     denda_tambahan_per_5_hari = 5500
# # #menghitung denda dasar
# #     denda = hari_terlambat * denda_per_hari
# # #jika keterlambatan lebih dari 10 hari,tambahkan denda tambahan
# #     if hari_terlambat > 10:
        
# # #hitung berapa banyak kelipatan 5 hari keterlambatan setelah 10 hari pertama
# #         sisa_hari = hari_terlambat - 5
# #         denda_tambahan = (sisa_hari // 5) * denda_tambahan_per_5_hari
# #         denda += denda_tambahan
        
# # #menampilkan hasil perhitungan denda
# #     print(f"total denda keterlambatan:Rp{denda}")
# # #menanyakan apakah ingin menghitung kembali 
# #     ulang =input("apakah anda ingin menghitung kembali?(y/n):")
# #     if ulang != 'y':
# #         print("terima kasih,sampai jumpa!")
# #     break




# #tugas membuat program denda keterlambatan pinjaman DVD
# jawab="ya"

# while (jawab == ("ya")):
#     lama_pinjaman=int(input("berapa hari anda meminjam dvd:"))
#     denda = 0
#     if lama_pinjaman < 5:
#         for i in range(6,lama_pinjaman+1):
#             denda+=2500
#             if i % 10 == 0:
#                 denda+=5500
#         print(f"anda terlambat mengembalikan dvd selama {lama_pinjaman -5} hari, anda harus membayar denda sebesar:",denda)
#         jawaban =(input("ingin menghitung ulang? (ya/tidak?):"))
#         if jawaban == "tidak":
#             break
#     else:
#         print("anda tepat waktu")
#         jawab=(input("ingin menghitung ulang? (ya/tidak?):"))
#         if jawab != "ya":
#             break





while True :
    lama_sewa = int(input("masukkan lama penyewaan DVD : "))
    denda_pokok = 2500
    denda_tambahan = 5500

    if lama_sewa <= 5 :
        print(("anda mengembalikkan tepat waktu"))
    else :
        keterlambatan = lama_sewa - 5 
        denda = keterlambatan * denda_pokok

        if keterlambatan > 10 :
            denda_tambahan = (keterlambatan // 5) * denda_tambahan
            denda += denda_tambahan 

        print("total denda keterlambatan yang anda bayar adalah : Rp", denda)

    lanjut = input("Ingin menghitung lagi? (ya/tidak): ")
    if lanjut != 'ya':
        break
    
    