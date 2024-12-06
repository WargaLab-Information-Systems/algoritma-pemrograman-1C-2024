def cek_palindrom(kata):
    # Ubah huruf menjadi huruf kecil dan hilangkan spasi
    kata = kata.lower().replace(" ", "")
    
    # Bandingkan string asli dengan string yang dibalik
    return kata == kata[::-1]

# Contoh penggunaan
print(cek_palindrom("Kasur ini rusak"))  # True
print(cek_palindrom("katak"))            # True
print(cek_palindrom("halo dunia"))       # False