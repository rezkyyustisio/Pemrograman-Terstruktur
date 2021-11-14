# Program untuk menyeleksi kriteria umur

print("Rezky Yustisio Hadi Pratama 3201816021")
print("Kategori umur ")

# Menginputkan usia
usia = int(input("Masukkan usia anda "))

# Proses
if usia <= 5:
	hasil = "Balita"
elif 5 < usia and usia <= 13:
	hasil = "Anak Anak"
elif 13 < usia and usia <= 25:
	hasil = "Remaja"
else:
	hasil = "Tidak terdefinisi"
	
# Tampilkan hasil
print("Kategori usia %s tahun adalah %s" % (usia, hasil))

