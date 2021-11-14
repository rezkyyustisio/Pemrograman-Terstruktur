# Latihan 4
awal = int(input("Masukkkan Nilai Awal "))
akhir = int(input("Masukkan Nilai Akhir "))

count = 0
summ = 1

print("Bilangan antara %s dan %s " % (awal, akhir))

for i in range(awal, akhir, 3):
	print(i)
	count = count + 1
	summ = summ * i

print("Bilangan diatas ada %s bilangan " % count)
print("Jumlah keseluruhan bilangan adalah = %s " %summ)