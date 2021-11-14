ip = float(input("Masukkan nilai IP "))
if ip > 2 and ip <= 2.75:
    print("Lulus memuaskan")
elif ip >= 2.75 and ip < 3.5:
    print("Lulus sangat memuaskan")
elif ip >= 3.5 and ip <= 4.00:
    print("Lulus dengan pujian")
else:
    print("Data ip tidak valid")
