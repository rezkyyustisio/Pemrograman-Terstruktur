class Pesawat:
	def __init__(self, namaPesawat, umurPesawat, kodePenerbangan, waktuPenerbangan):
		self.namaPesawat = namaPesawat
		self.umurPesawat = umurPesawat
		self.kodePenerbangan = kodePenerbangan
		self.waktuPenerbangan = waktuPenerbangan
	def maju(self):
		return "Maju"
	def mundur(self):
		return "Mundur"
	def landing(self):
		return "Mendarat"
	def takeOff(self):
		return "Terbang"
garuda = Pesawat("garuda", 18, 2019, "10.00 Wib")
print("Pesawat %s dengan kode penerbangan %s akan %s pada jam %s" % (garuda.namaPesawat, garuda.kodePenerbangan, garuda.takeOff(), garuda.waktuPenerbangan))