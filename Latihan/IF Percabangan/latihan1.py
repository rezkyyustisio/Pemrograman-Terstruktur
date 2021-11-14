def main():
    bilangan = int(input("Masukkan bilangan bulat "))

    #memeriksa bilangan, genap dan tidak
    if(bilangan % 2 == 0):
        print("%d adalah bilangan genap" % bilangan)
    else:
        print("%d adalah bilangan ganjil" % bilangan)

if __name__ == "__main__":
    main()
