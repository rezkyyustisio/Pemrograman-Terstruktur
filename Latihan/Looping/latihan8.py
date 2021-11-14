# Tuple nested (tuple bersarang)
# Tuple diisi tuple
tuple1 = ("aku", "cinta", "kamu")
tuple2 = ("selama", 3, "tahun")
tuple3 = (tuple1, tuple2)

# Mengeluarkan isi dari tuple 3
print(tuple3)
# Mengeluarkan isi tuple1
print(tuple3[0])
# Mengeluarkan isi tuple2
print(tuple3[1])
# Mengeluarkan isi tuple 2 dengan indeks 0 dari tuple3
print(tuple3[1][0])