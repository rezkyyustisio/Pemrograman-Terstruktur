print("""
----------------------------------
| Kelompok 5 			 |
| 1. Rezky Yustisio Hadi Pratama |
| 2. Roby Wahydi 		 |
| 3. Nurhidayah 		 |
| 4. Dalillah Nia Ayuni		 |
| 5. Ayu Wandira		 |
----------------------------------
""")
print("""
	=============================================
		GAMES (BATU, GUNTING, KERTAS)
	=============================================
""")
nama = input("Masukkan nama anda: ")
if nama != "":
	print("""
Tingkat Kesulitan:
1. Mudah
2. Sedang
3. Sulit
Note: untuk tingkat mudah, akan diberi clue
	""")
	komputer = {
		1 : ["batu", "gunting", "kertas", "kertas", "gunting", "batu"],
		2 : ["kertas", "batu", "kertas", "batu", "kertas", "batu"],
		3 : ["gunting", "gunting", "gunting", "kertas", "kertas", "batu"]
	}
	pilihan_user = int(input("Masukkan salah satu nomor diatas yang anda inginkan (1, 2, 3) : "))
	if pilihan_user == 1:
		print("Clue: keras, pemotong, kulit pohon, warna putih, 2 lobang, bulat")
	for nomor in komputer:
		if pilihan_user == nomor:
			skor_user = 0
			skor_komputer = 0
			skor_pemenang = 3
			mulai = True
			while mulai:
				for i in range(0, 6):

					if skor_user == skor_pemenang:
						print("Selamat %s kamu menang" % (nama))
						mulai = False
						break

					if skor_komputer == skor_pemenang:
						print("Kamu kalah, terimakasih telah bermain")
						mulai = False
						break

					senjata_user = input("Masukkan (batu, gunting, kertas) : ")

					if senjata_user == komputer[nomor][i]:
						print(">>> S E R I <<<")
						print("Jawaban komputer : ", komputer[nomor][i])
						print("Skor anda: ", skor_user)
						print("Skor komputer: ", skor_komputer)
						print()
					elif senjata_user == "batu":
						if komputer[nomor][i] == "gunting":
							skor_user = skor_user + 1
							print("===>>> Menang <<<===")
							print("Jawaban komputer : ", komputer[nomor][i])
							print("Skor anda: ", skor_user)
							print("Skor komputer: ", skor_komputer)
							print("=" * 30)
							print()
						elif komputer[nomor][i] == "kertas":
							skor_komputer = skor_komputer + 1
							print("===>>> Kalah <<<===")
							print("Jawaban komputer : ", komputer[nomor][i])
							print("Skor anda: ", skor_user)
							print("Skor komputer: ", skor_komputer)
							print("=" * 30)
							print()
					elif senjata_user == "gunting":
						if komputer[nomor][i] == "kertas":
							skor_user = skor_user + 1
							print("===>>> Menang <<<===")
							print("Jawaban komputer : ", komputer[nomor][i])
							print("Skor anda: ", skor_user)
							print("Skor komputer: ", skor_komputer)
							print("=" * 30)
							print()
						elif komputer[nomor][i] == "batu":
							skor_komputer = skor_komputer + 1
							print("===>>> Kalah <<<===")
							print("Jawaban komputer : ", komputer[nomor][i])
							print("Skor anda: ", skor_user)
							print("Skor komputer: ", skor_komputer)
							print("=" * 30)
							print()
					elif senjata_user == "kertas":
						if komputer[nomor][i] == "batu":
							skor_user = skor_user + 1
							print("===>>> Menang <<<===")
							print("Jawaban komputer : ", komputer[nomor][i])
							print("Skor anda: ", skor_user)
							print("Skor komputer: ", skor_komputer)
							print("=" * 30)
							print()
						elif komputer[nomor][i] == "gunting":
							skor_komputer = skor_komputer + 1
							print("===>>> Kalah <<<===")
							print("Jawaban komputer : ", komputer[nomor][i])
							print("Skor anda: ", skor_user)
							print("Skor komputer: ", skor_komputer)
							print("=" * 30)
							print()