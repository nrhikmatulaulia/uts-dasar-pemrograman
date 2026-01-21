print("\nAPLIKASI PENGHITUNG LUAS DAN KELILING BANGUN DATAR")
nama = input("\nMasukkan nama anda: ")
print("Halo", nama)

daftarbangundatar =["1. persegi " "2. persegi panjang " "3. segitiga " "4.lingkaran"]
print(daftarbangundatar)

def persegi():
    print("Anda memilih persegi")
    sisi = int(input("Masukkan nilai sisi: "))
    luas = sisi*sisi
    keliling = 4 * sisi
    print("Luas persegi:", luas)
    print("Keliling persegi:", keliling)
def persegi_panjang():
    print("Anda memilih persegi_panjang")
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))
    luas = panjang*lebar
    keliling = 2*(panjang+lebar)
    print("Luas persegi_panjang:", luas)
    print("Keliling persegi_panjang:", keliling)
def segitiga():
    print("Anda memilih segitiga")
    alas = int(input("Masukkan nilai alas: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    luas = 0.5*alas*tinggi
    keliling = alas+alas+alas
    print("Luas segitiga:", luas)
    print("Keliling segitiga:", keliling)
def lingkaran():
    print("Anda memilih lingkaran")
    jari_jari = int(input("Masukkan nilai jari-jari: "))
    luas = 3.14*jari_jari*jari_jari
    keliling = 2 * 3.14 * jari_jari
    print("Luas ligkaran:", luas)
    print("Keliling lingkaran:", keliling)
    
pilih = input("\nSilahkan pilih bangun datar (1-4): ")
if pilih == "1":
    persegi()
elif pilih == "2":
    persegi_panjang()
elif pilih == "3":
    segitiga()
elif pilih == "4":
    lingkaran()
else:
    print("\nInput tidak valid, silahkan pilih bangun daftar dari(1-4): ")
    
while True:
    hitung_lagi = input("\nApakah anda ingin menghitung lagi? (Ya/Tidak): ")
    if hitung_lagi == "Ya":
        pilih = input("\nSilahkan pilih bangun datar dari (1-4): ")
        if pilih == "1":
           persegi()
        elif pilih == "2":
           persegi_panjang()
        elif pilih == "3":
            segitiga()
        elif pilih == "4":
            lingkaran()
        else:
            print("\nInput tidak valid, Silahkan pilih bangun datar dari (1-4):")
    elif hitung_lagi == "Tidak":
        print("Baiklah, Terimakasih telah menggunakan program ini. ")
        break
    else:
        print("Input tidak valid, Silahkan jawab 'Ya/Tidak'.")