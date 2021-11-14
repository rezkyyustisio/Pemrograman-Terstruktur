# Program sederhana menampilkan bilangan terbesar dari 3 bilangan 

print("Rezky Yustisio Hadi Pratama 3201816021")

print("Nilai maksimum dari tiga bilangan ")

# Menginputkan bilangan
bilangan_1 = int(input("Masukkan bilangan ke-1 "))
bilangan_2 = int(input("Masukkan bilangan ke-2 "))
bilangan_3 = int(input("Masukkan bilangan ke-3 "))

# Proses
if bilangan_1 > bilangan_2 and bilangan_1 > bilangan_3:
	hasil = bilangan_1

if bilangan_2 > bilangan_1 and bilangan_2 > bilangan_3:
	hasil = bilangan_2

if bilangan_3 > bilangan_1 and bilangan_3 > bilangan_2:
	hasil = bilangan_3

# Tampilkan hasil
print("Bilangan terbesar adalah ", hasil)
