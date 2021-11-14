class Bunga:
	def __init__(self, ukuran_bunga):
		self.ukuran = ukuran_bunga
class BungaBesar(Bunga):
	def detail_bunga(self):
		if self.ukuran == "besar":
			besar = {
				"raflesia" : {
					"ciri bunga" : {
						"warna" : "merah",
						"ukuran" : "besar",
						"habitat" : "darat"
					}
				},
				"bangkai" : {
					"ciri bunga" : {
						"warna" : "hijau",
						"ukuran" : "besar",
						"habitat" : "darat"
					}
				},
				"palem" : {
					"ciri bunga" : {
						"warna" : "kuning",
						"ukuran" : "besar",
						"habitat" : "darat"
					}
				}
			}

			no = 0
			for i, k in besar.items():
				no = 1 + no
				print("%s. %s" % (no, i))
			print()

			inputan_nama = input("Masukkan nama bunga: ")
			for i in besar:
				if inputan_nama == i:
					print()
					print("Ciri-Ciri bunga sebagai berikut: ")
					for j in besar[i]["ciri bunga"]:
						print("%s => %s" % (j,besar[i]["ciri bunga"][j]))
		
class BungaKecil(Bunga):
	def detail_bunga(self):
		if self.ukuran == "kecil":
			kecil = {
				"melati" : {
					"ciri bunga" : {
						"warna" : "putih",
						"ukuran" : "kecil",
						"habitat" : "darat"
					}
				},
				"mawar" : {
					"ciri bunga" : {
						"warna" : "merah",
						"ukuran" : "kecil",
						"habitat" : "darat"
					}
				},
				"kenanga" : {
					"ciri bunga" : {
						"warna" : "kuning",
						"ukuran" : "kecil",
						"habitat" : "darat"
					}
				}
			}
			no = 0
			for i, k in kecil.items():
				no = 1 + no
				print("%s. %s" % (no, i))
			inputan_nama = input("Masukkan nama bunga: ")
			for i in kecil:
				if inputan_nama == i:
					print()
					print("Ciri-Ciri bunga sebagai berikut: ")
					for j in kecil[i]["ciri bunga"]:
						print("%s => %s" % (j,kecil[i]["ciri bunga"][j]))

print("""
Bunga:

1. besar
2. kecil
""")
inputan_ukuran = input("Masukkan ukuran bunga : ")
print()
for b in (BungaBesar(inputan_ukuran), BungaKecil(inputan_ukuran)):
	b.detail_bunga()




