data_mahasiswa = {'nama':'Rezky Yustisio Hadi Pratama',
	'nim':'3201816021',
	'prodi':'Teknik Informatika',
	'email':'rezkyyustisio@gmail.com',
	'website':'rezkyyustisio.com',
	'social media':{
		'facebook':'rezky yustisio hadi pratama',
		'instagram':'rezkyyustisio'
	}
}
# menampilkan data dictionary
# memanggil nama list nya diikuti dengan isi dari list yang ditampiklkan

# Cara pertama
masukkan = str(input("Masukkan nim "))
if masukkan == data_mahasiswa['nim']:
	for data in data_mahasiswa:
		print(data,':',data_mahasiswa[data])
else:
	print("Data anda tidak ditemukan")
print("--------------------------------")

# Cara kedua
for i, z in data_mahasiswa.items():
	print("%s : %s" % (i,z))
