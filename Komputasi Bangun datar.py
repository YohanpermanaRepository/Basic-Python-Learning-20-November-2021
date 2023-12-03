def persegi(panjang,lebar):
    luaspersegi=panjang*lebar
    return luaspersegi
def jargen(alas,tinggi):
    luasjargen=alas*tinggi
    return luasjargen
def segitiga(alas,tinggi):
    luassegitiga=1/2 * alas * tinggi
    return luassegitiga
def lingkaran(jarijari):
    luaslingkaran=22/7 * jarijari**2
    return luaslingkaran
def contact():
    print("<==========================>")
    print("|      CONTACT PERSON      |")
    print("| Nama : Nuri Yohan Permana|")
    print("| NIM  : 210441100052      |")
    print("| Kelas: SI 1D             |")
    print("| WA   : 000000000000      |")
    print("<==========================>")



select = "y"
while select == "y" :
    print("<============================================================>")
    print("Ingin Menghitung Luas Bangun Datar Apa?")
    print("<============================================================>")
    print("1. Persegi")
    print("2. Jajargenjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("<============================================================>")

    pilih=int(input("Pilih sesuai nomor yang ingin anda pilih!!"))

    if pilih==1:
        p = int(input("Masukkan panjang : "))
        l = int(input("Masukkan Lebar : "))
        print("Luas Persegi panjang dengan panjang ",p,"cm ","dan lebar ",l,"adalah : ",persegi(p,l)," cm")
    elif pilih==2:
        a = int(input("Masukkan Alas : "))
        t = int(input("Masukkan Tinggi : "))
        print("Luas Jajargenjang dengan alas ",a,"cm ","dan tinggi ",t,"adalah : ",jargen(a,t)," cm")
    elif pilih==3:
        al = int(input("Masukkan Alas : "))
        tg = int(input("Masukkan Tinggi : "))
        print("Luas Segitiga dengan alas ", al, "cm ", "dan tinggi ", tg, "adalah : ", segitiga(al,tg), " cm")
    elif pilih==4 :
        r = int(input("Masukkan Jari-jari Lingkarannya : "))
        print("Luas Lingkaran dengan jari-jari ",r,"adalah : ",lingkaran(r), " cm")
    else :
        print("Maaf anda salah menginputkan!!")

    select = input("INGIN MENGHITUNG LAGI ? (y/t) : ")
    if select=="y":
        continue
    elif select=="t":
        print("TERIMAKASIH TELAH MENCOBA PROGRAM HITUNG LUAS BANGUN DATAR SAYA")
        contact()
        break
    else :
        print("Maaf anda salah menginputkan!!")