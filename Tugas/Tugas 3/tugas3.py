print()
print("Terdiri dari 5 soal")
print()
soal_jawaban = {
	"html" : "Bahasa yang terdiri dari tag-tag",
	"css" : "Bahasa untuk merancang, merubah, mendesain, membentuk halaman wesite",
	"php" : "Bahasa pemrograman server side untuk pembuatan website dinamis yang di awali dengan tag <?php",
	"python" : "Bahasa yang identik dengan ular ",
	"pascal" : "Bahasa pemrograman yang pertama kali di buat oleh Profesor Niklaus Wirth"
}
skor = 0
no_soal = 0
for i in soal_jawaban:
	no_soal = no_soal + 1
	print("%s. %s" % (no_soal, soal_jawaban[i]))
	print()
	jawaban_user = input("Masukkan jawaban kamu: ")
	if jawaban_user.lower() == i:
		print("Jawaban kamu benar :)")
		skor = skor + 10
		print("Skor kamu adalah ", skor)
		lanjut = input("Ingin lanjut atau tidak ? ")
		if lanjut.lower() == "tidak":
			print("Terimakasih telah menjawab")
			print()
			break;
		print()
	else:
		skor = skor - 5
		print("Jawaban kamu salah :(")
		print("Jawabannya adalah : %s" % (i))
		print("Skor kamu adalah ", skor)
		print()



