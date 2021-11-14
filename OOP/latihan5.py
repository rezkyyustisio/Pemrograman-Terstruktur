class Rumah:
	def __init__(self, nama, tipe, luasRumah):
		self.nama = nama
		self.tipe = tipe
		self.luasRumah = luasRumah
	def cetak(self):
		print("Detail Rumah ", self.nama)
		print("Luas rumah : ", self.luasRumah)
		print("Tipe rumah : ", self.tipe)
class RumahMewah(Rumah):
	def fasilitas(self):
		print("""
Fasilitas yang diberikan:
1. Ac
2. Kolam Renang
3. Tingkat 2
		""")
class RumahStandar(Rumah):
	def fasilitas(self):
		print("""
Fasilitas yang diberikan:
1. Kipas Angin
2. Sumur
3. Tingkat 1
		""")

print()
nama = input("Masukkan nama anda: ")
luasRumah = int(input("Masukkan luas rumah: "))
tipeRumah = input("Masukkan tipe rumah (mewah, standar): ")
print()
if str.lower(tipeRumah) == "mewah":
	mewah = RumahMewah(nama, luasRumah, tipeRumah)
	mewah.cetak()
	mewah.fasilitas()
elif str.lower(tipeRumah) == "standar":
	standar = RumahStandar(nama, tipeRumah, luasRumah)
	standar.cetak()
	standar.fasilitas()
