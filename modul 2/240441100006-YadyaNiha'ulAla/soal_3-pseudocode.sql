START

# Inisialisasi Jaka
SET jaka_nama = "Jaka"
SET jaka_skor = 1100
SET jaka_ipk = 3.5

# Inisialisasi Ida
SET ida_nama = "Ida"
SET ida_skor = 1000
SET ida_ipk = 3.5

# Inisialisasi persyaratan beasiswa
SET p_skor = 1100
SET p_ipk = 3.0

PRINT "Hasil Kelulusan Beasiswa:"

# Cek kelulusan Jaka
IF jaka_skor > p_skor AND jaka_ipk >= p_ipk THEN
    PRINT "Jaka Lulus Persyaratan Beasiswa"
ELSE
    PRINT "Jaka Tidak Lulus Persyaratan Beasiswa"
END IF

# Cek kelulusan Ida
IF ida_skor > p_skor AND ida_ipk >= p_ipk THEN
    PRINT "Ida Lulus Persyaratan Beasiswa"
ELSE
    PRINT "Ida Tidak Lulus Persyaratan Beasiswa"
END IF

END
