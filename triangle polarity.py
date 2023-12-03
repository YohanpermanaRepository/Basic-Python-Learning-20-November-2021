def pola():
    angka = int(input("Masukkan Angka : "))
    for i in range(0, angka):
        for segitiga in range(0, i + 1):
            print("* ", end= " ")
        print(" ")
pilih =str(input("Ingin Menampilkan Pola segitiga?? (y/t) "))
if pilih=="y":
    pola()
elif pilih=="t":
    print("Terimakasih")
else:
    print("Maaf code yang anda masukkan salah!!")