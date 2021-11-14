tahun_kabisat = int(input("Masukkan tahun kabisat "))
if tahun_kabisat % 4 != 0:
    print("%d ini bukan tahun kabisat" %tahun_kabisat)
elif tahun_kabisat % 100 == 0:
    print("%d ini bukan tahun kabisat" %tahun_kabisat)
else:
    print("Ini adalah kabisat")
