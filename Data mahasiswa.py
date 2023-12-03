list_nim =[]
list_nama = []
list_prodi = []
list_alamat = []

for x in range(5):
    print("========================================")
    print("DATA MAHASISWA ", x+1)
    print("========================================")
    nim = (input("Masukkan NIM : "))
    nama = (input("Masukkan Nama : "))
    prodi = (input("Masukkan Program Studi : "))
    alamat = (input("Masukkan Alamat : "))

    print("")
    list_nim.append(nim)
    list_nama.append(nama)
    list_prodi.append(prodi)
    list_alamat.append(alamat)
    tuple_nim = tuple(list_nim)
    tuple_nama = tuple(list_nama)
    tuple_prodi = tuple(list_prodi)
    tuple_alamat = tuple(list_alamat)
    x += 1

    if len(tuple_prodi) == 5:
        print("========================================")
        print("DATA MAHASISWA ")
        print("========================================")
        for n,u,r,i in zip(tuple_nim,tuple_nama,tuple_prodi,tuple_alamat):
            if len(tuple_prodi) == 5 :
                print("")
                print("NIM : " + str(int(n)))
                print("Nama : " + str(u))
                print("Prodi : " + str(r))
                print("Alamat : " + str(i))

select = "y"
while select == "y" :
    select = input("INGIN MENAMPILKAN BERDASARKAN PRODI ??? (y/t) : ")
    if select=="y":
        pilih = input("Masukkan Prodi yang ingin anda cari : ")
        print("========================================")
        print("DATA MAHASISWA BERPRODI ", pilih)
        print("========================================")
        for j in range(5):
            if pilih == tuple_prodi[j]:
                print("|-> NIM       : ",tuple_nim[j])
                print("|-> Nama      : ",tuple_nama[j])
                print("|-> Prodi     : ",tuple_prodi[j])
                print("|-> Alamat    : ",tuple_alamat[j])
                print("========================================")
                continue
            elif pilih != tuple_prodi[j]:
                continue
            else:
                print("Prodi tidak ada")
                continue
    elif select=="t":
        print("TERIMAKASIH TELAH MENCOBA PROGRAM SAYA")
        break
    else :
        print("Maaf anda salah menginputkan!!")
