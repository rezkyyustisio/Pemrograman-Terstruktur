class Dog:
	def __init__(self, nama, umur, warna):
		self.nama = nama
		self.umur = umur
		self.warna = warna
	def lari(self):
		print("Lari dengan kencang")
Guguk = Dog("budds", 8, "coklat")
Guguk.nama = "Si Guguk"
Guguk.lari()
