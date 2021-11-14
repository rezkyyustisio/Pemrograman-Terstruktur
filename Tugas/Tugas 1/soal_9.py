# Program penentuan nilai indeks ujian

print("Rezky Yustisio Hadi Pratama 3201816021")

print("Program nilai indeks Mahasiswa ")

# Menginputkan nilai UTS dan UAS
nilai_uts = float(input("Masukkan nilai UTS "))
nilai_uas = float(input("Masukkan nilai UAS "))

# Proses
nilai = 60 / 100 * nilai_uts + 40 / 100 * nilai_uas

if nilai >= 80:
	hasil = "A"
elif 80 > nilai and nilai >= 70:
	hasil = "B"
elif 70 > nilai and nilai >= 55:
	hasil = "C"
elif 55 > nilai and nilai >= 40:
	hasil = "D"
elif nilai < 40:
	hasil = "E"

# Tampilkan hasil
print("Total nilai akhir adalah : ", nilai)
print("Nilai indeks : ", hasil)