# Program mengkonversi waktu ke satuan detik

print("Rezky Yustisio Hadi Pratama 3201816021")

print("Konversi jam ke detik")

# Menginputkan jam, menit, detik
jam = int(input("Masukkan jumlah jam "))
menit = int(input("Masukkan jumlah menit "))
detik = float(input("Masukkan jumlah detik "))

# Proses
konversi_detik = jam * 3600 + menit * 60 + detik

# Tampilkan hasil
print("%s:%s:%s adalah sama dengan %s " % (jam, menit, detik, konversi_detik))


