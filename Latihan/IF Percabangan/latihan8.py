print("Aplikasi Menghitung Konversi Suhu")
print("1. Konversi suhu Celcius ke Reamur")
print("2. Konversi suhu Celcius ke Fahrenheit")
pilihan = int(input("Masukkan nomor diatas yang ingin di konversikan "))

# Konversi dari Celcius ke Reamur
if pilihan == 1:
    celcius = int(input("Masukkan nilai Celcius "))
    proses = 4 / 5 * celcius
    print("Hasil dari %s Celcius ke Reamur adalah %s " % (celcius, proses))
# Konversi dari Celcius ke Fahrenheit
elif pilihan == 2:
    celcius = int(input("Masukkan nilai Celcius "))
    proses = 9 / 5 * celcius + 32
    print("Hasil dari %s Celcius ke Fahrenheit adalah %s " % (celcius, proses))
else:
    print("Nomor yang anda masukkan tidak ada di pilihan")
