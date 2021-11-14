def penjumlahan(bil1, bil2):
    penjumlahan = bil1 + bil2
    return penjumlahan

def pengurangan(bil1, bil2):
    pengurangan = bil1 - bil2
    return pengurangan

def perkalian(bil1, bil2):
    perkalian = bil1 * bil2
    return perkalian

def pembagian(bil1, bil2):
    pembagian = bil1 / bil2
    return pembagian

def modulus(bil1, bil2):
    modulus = bil1 % bil2
    return modulus

print(
"""
Operasi hitung:
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Modulus

Masukkan salah satu nomor diatas yang ingin di operasikan
""")

nomor = int(input("Masukkan nomor: "))
bilangan_1 = float(input("Masukkan bilangan ke-1 "))
bilangan_2 = float(input("Masukkan bilangan ke-2 "))

if nomor == 1:
    print("Anda memilih operasi penjumlahan")
    hasil = penjumlahan(bilangan_1, bilangan_2)
    print("Hasil dari %s + %s adalah %s" % (bilangan_1, bilangan_2, hasil))
elif nomor == 2:
    print("Anda memilih operasi pengurangan")
    hasil = pengurangan(bilangan_1, bilangan_2)
    print("Hasil dari %s - %s adalah %s" % (bilangan_1, bilangan_2, hasil))
elif nomor == 3:
    print("Anda memilih operasi perkalian")
    hasil = perkalian(bilangan_1, bilangan_2)
    print("Hasil dari %s * %s adalah %s" % (bilangan_1, bilangan_2, hasil))
elif nomor == 4:
    print("Anda memilih operasi pembagian")
    hasil = pembagian(bilangan_1, bilangan_2)
    print("Hasil dari %s : %s adalah %s" % (bilangan_1, bilangan_2, hasil))
elif nomor == 5:
    print("Anda memilih operasi modulus")
    hasil = modulus(bilangan_1, bilangan_2)
    print("Hasil dari %s modulus %s adalah %s" % (bilangan_1, bilangan_2, hasil))
else:
    print("Nomor yang anda masukkan tidak ada di daftar operasi perhitungan")
