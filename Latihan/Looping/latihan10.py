daftar_teman = ['Arsyad', 'Alvian', 'Irfan', 'Roby', 'Aldi']

# Method
daftar_teman.insert(1, "Rezky")
daftar_teman.append("Lazuardi")
del daftar_teman [3]
daftar_teman.remove("Lazuardi")
# Akhir

for i in range(0,len(daftar_teman)):
	print("Teman saya adalah %s" % (daftar_teman[i]))

print("Teman saya dengan indeks 3 adalah %s" % (daftar_teman[2]))
print("Total teman %s" % len(daftar_teman))

# Method
# append untuk menambahkan data di ujung list
# insert untuk menambahkan data dengan urutan tertentu di sebuah list
# del untuk menghapus data di urutan tertentu