# Sequence unpacking
# Tuple data_diri
data_diri = ("aisyah", 17, "perempuan", "memasak")
data_rumah = ["Komp. Griya Husada", "Blok P27"]

# unpacking tuple
nama,umur,gender,hobi = data_diri

# unpacking list
komp,blok = data_rumah

# memanggil isi tuple dengan variabel sebelumnya
print(nama)
print(nama,gender)

# memanggil isi list dengan variabel sebelumnya
print(komp)