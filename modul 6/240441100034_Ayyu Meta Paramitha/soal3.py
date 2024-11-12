barang = []

def tambah_barang():
    while True:
        nama_barang = input("Masukkan Nama Barang: ")
        id_barang = input("Masukkan ID Barang: ")
        prioritas = input("Masukkan Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")

        while True:
          if prioritas.lower() in ('darurat', 'biasa', 'non-darurat'):
              break
          else:
              print('Input tidak valid, silakan masukkan ulang')
              prioritas = input("Masukkan Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")
              
        if prioritas.lower() == 'darurat':
            barang.insert(0, (nama_barang, id_barang, prioritas))
        elif prioritas.lower() == 'biasa':
            barang.insert(len(barang) // 2, (nama_barang, id_barang, prioritas))
        else:
            barang.append((nama_barang, id_barang, prioritas))


        tambah_lagi = input("Apakah ingin menambahkan barang lagi? (ya/tidak): ")
        if tambah_lagi.lower() != 'ya':
            break
    
    print("Daftar Barang:")
    for i, (nama, id_barang, prioritas) in enumerate(barang):
        print(f"{i+1}. {nama} ID: {id_barang} {prioritas}" )

tambah_barang()
