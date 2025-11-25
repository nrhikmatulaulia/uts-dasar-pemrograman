# aplikasi_dekomposisi_angka.py
try:
    angel_input = int(input("Masukkan angka (0 s.d.  3600000): "))
    
    if 0 <= angel_input <= 3600000:
        jutaan = angel_input // 1000000
        sisa_jutaan = angel_input % 1000000
        
        ratusan_ribu = sisa_jutaan // 100000
        sisa_ratusan_ribu = sisa_jutaan % 100000
        
        puluhan_ribu = sisa_ratusan_ribu // 10000
        sisa_puluhan_ribu = sisa_ratusan_ribu % 10000
        
        ribuan = sisa_puluhan_ribu // 1000
        sisa_ribuan = sisa_puluhan_ribu % 1000
        
        ratusan = sisa_ribuan // 100
        sisa_ratusan = sisa_ribuan % 100
        
        puluhan = sisa_ratusan // 10
        satuan = sisa_ratusan % 10
        
        # Header output (tanpa warna agar portable)
        print("\nHasil Pemecahan Angka: ")
        
        print("--------------------------------------------------------")
        
    if angel_input >= 1000000:
        print("Jutaan         :", jutaan)
    if angel_input >=  100000:
        print("Ratusan Ribu   :", ratusan_ribu)
    if angel_input >= 10000:
        print("Puluhan Ribu   :", puluhan_ribu)
    if angel_input >= 1000:
        print("Ribuan         :", ribuan)
    if angel_input >= 100:
        print("Ratusan        :", ratusan)
    if angel_input >= 10:
        print("Puluhan        :", puluhan)
    if angel_input >= 1:
        print("Satuan         :", satuan)
        
        print("--------------------------------------------------------")
        
        print("Pemecahan angka selesai.")
    else:
        print("Silahkan masukkan angka yang sesuai (0 s.d. 3600000).")
except ValueError:
    print("Input salah. Silahkan masukkan angka yang benar.")
    