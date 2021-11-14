def halo(nama):
    print("Halo %s!" % (nama))
def cetak_maksimal(a, b):
    if a > b:
        print("%s merupakan nilai maksimal " % (a))
    elif a == b:
        print("%s sama dengan %s " % (a, b))
    else:
        print("%s merupakan nilai maksimal" % (b))
halo('Cantik')
halo('Ganteng')

cetak_maksimal(10, 100)

x = 3
y = 5

cetak_maksimal(x,y)
