user ={"Nama":"Nuri Hidayatuloh","Username":"Nuri1234","Skor":0,"Password":1234}
def tebak(z):
    if z == jumlah:
        print("Tebakan Anda Benar!!")
        print("Selamat Skor anda bertambah 50")
        user["Skor"] = user["Skor"] + 50
        for p in user:
            if p == "Nama":
                print("=>", p, ":", user[p])
            elif p == "Username":
                pass
            elif p == "Skor":
                print("=>", p, ":", user[p])
            else :
                break
    else:
        print("Tebakan Anda Salah!!")
        for p in user:
            if p == "Nama":
                print("=>", p, ":", user[p])
            elif p == "Username":
                pass
            elif p == "Skor":
                print("=>", p, ":", user[p])
            else:
                break
    return z
while True:
    user["Username"] = input("Silahkan Masukkan Nama User Anda :")
    username = user["Username"]
    user["Password"] = input("Silahkan Masukkan Password anda:")
    password = user["Password"]
    if username == "Nuri1234" and password == "1234":
        print('Login Berhasil!!!')

        print ('\n')
        print ("WELCOME", user['Nama'], "Mau Menghitung apa ?")

        break
    elif username != "Nuri1234" and password != "1234":
        print('Maaf Username dan Password anda salah!! Mohon inputkan ulang!')
    elif username != "Nuri1234":
        print('Maaf Username anda salah!! Mohon inputkan ulang!')
    elif password != "1234":
        print('Maaf, Password anda salah!! Mohon menginputkan ulang!!')
    else:
        print('Username dan Password anda salah!!')

program = "PERHITUNGAN BANGUN RUANG KOMPLEX"
qwe = "="*50
print(program.center(50, "="))
while True:
    pilih = ["Balok", "Kubus","Tabung","Kerucut","Keluar"]
    for abc in range(0, len(pilih)):
        print(f'{abc + 1}. {pilih[abc]}')
    print(qwe)
    bangun_pilihan = input("Silahkan masukkan ingin mencoba menu apa [1-5]: ")
    print(qwe)
    if bangun_pilihan == "1":
        print("Anda memilih perhitungan bangun ruang BALOK")
        rumus = ["Luas Permukaan","Volume"]
        for iii in range(0, len(rumus)):
            print (f'{iii + 1}. {rumus[iii]}')
        pilihan = input("Pilih ingin menghitung apa?[1-2]: ")
        if pilihan == "1":
            def hitung_luas_balok (panjang,lebar,tinggi):
                return 2* ((panjang*lebar) + (panjang * tinggi) + (lebar*tinggi))
            for balok in range(3):
                if balok == 0:
                    while True:
                        a = int (input("Masukkan panjang balok :"))
                        if a <=0 :
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else :
                            break
                if balok == 1:
                    while True:
                        b = int (input("Masukkan lebar balok :"))
                        if b <=0 :
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else:
                            break
                if balok == 2:
                    while True:
                        c = int (input("Masukkan tinggi balok :"))
                        if c <=0 :
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else:
                            break
            jumlah = hitung_luas_balok (a,b,c)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Luas Permukaan Balok = 2 ˟ (({a}˟{b}) + ({a} ˟ {c}) + ({b}˟{c})) = {jumlah}cm²')
        elif pilihan == "2":
            def hitung_volume_balok (panjang,lebar,tinggi):
                return panjang*lebar*tinggi
            for balok in range(3):
                if balok == 0:
                    while True:
                        a = int(input("Masukkan panjang balok :"))
                        if a <= 0:
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else:
                            break
                if balok == 1:
                    while True:
                        b = int(input("Masukkan lebar balok :"))
                        if b <= 0:
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else:
                            break
                if balok == 2:
                    while True:
                        c = int(input("Masukkan tinggi balok :"))
                        if c <= 0:
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else:
                            break
            jumlah = hitung_volume_balok (a,b,c)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Volume Balok = {a}˟{b}˟{c}={jumlah}cm³')
        else:
            print("Salah Input")
    elif bangun_pilihan == "2":
        print("Anda memilih bangun kubus")
        rumus = ["Volume","Luas","Keliling"]
        for aaa in range(0, len(rumus)):
            print (f'{aaa + 1}. {rumus[aaa]}')
        pilihan = input("Pilih rumus[1-3]: ")
        if pilihan == "1":
            def hitung_volume_kubus (sisi):
                return sisi*sisi*sisi
            while True:
                a = int (input("Masukkan sisi kubus :"))
                if a <= 0:
                    print("Maaf Masukkan angka Positif!!")
                    continue
                else:
                    break
            jumlah = hitung_volume_kubus (a)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Volume kubus : sisi³ = {a} ˟ {a} ˟ {a} = {jumlah}cm³')
        elif pilihan == "2":
            def hitung_luas_kubus (sisi) :
                return 6*sisi
            while True:
                a = int (input("Masukkan sisi kubus :"))
                if a <= 0:
                    print("Maaf Masukkan angka Positif!!")
                    continue
                else:
                    break
            jumlah = hitung_luas_kubus (a)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Luas Kubus = {a} ˟ 6 = {jumlah}cm²')
        elif pilihan == "3":
            def hitung_keliling_kubus (sisi):
                return 12*sisi
            while True:
                a = int (input("Masukkan sisi kubus :"))
                if a <= 0:
                    print("Maaf Masukkan angka Positif!!")
                    continue
                else:
                    break
            jumlah = hitung_keliling_kubus (a)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Keliling kubus = 12 ˟ {a} = {jumlah}cm²')
        else :
            print("Salah Input")
    elif bangun_pilihan == "3":
        print("Anda memilih bangun tabung")
        rumus = ["Volume","Keliling"]
        for sss in range(0, len(rumus)):
            print (f'{sss + 1}. {rumus[sss]}')
        pilihan = input("Pilih rumus[1-2]: ")
        if pilihan == "1":
            def hitung_volume_tabung (tinggi,r):
                π = 22/7
                return (π * (r*r))*tinggi
            for tabung in range(2):
                if tabung == 0:
                    while True:
                        a = int (input("Masukkan r  tabung:"))
                        if a <= 0:
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else:
                            break
                if tabung == 1:
                        while True:
                            b = int (input("Masukkan tinggi tabung :"))
                            if b <= 0:
                                print("Maaf Masukkan angka Positif!!")
                                continue
                            else:
                                break
            jumlah = hitung_volume_tabung (b,a)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Volume tabung = (π ˟ ({a}˟{a}))˟{b}={jumlah}cm³')

        elif pilihan == "2":
            def hitung_keliling_tabung (r):
                π = 22/7
                return 2* π * r
            for tabung in range(2):
                if tabung == 0:
                    while True:
                        a = int(input("Masukkan r  tabung:"))
                        if a <= 0:
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else:
                            break
                if tabung == 1:
                    while True:
                        b = int(input("Masukkan tinggi tabung :"))
                        if b <= 0:
                            print("Maaf Masukkan angka Positif!!")
                            continue
                        else:
                            break
            jumlah = hitung_keliling_tabung (a)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Volume tabung = 2 ˟ π ˟ {a} ={jumlah}cm²')
        else:
            print("Salah Input")
    elif bangun_pilihan == "4" :
        print("Anda memilih bangun Kerucut")
        rumus = ["Luas Permukaan","Volume"]
        for ddd in range(0, len(rumus)):
            print(f'{ddd + 1}. {rumus[ddd]}')
        pilihan = input("Pilih rumus[1-2]: ")
        if pilihan == "1":
            def hitung_luas_kerucut(s, r):
                π = 22 / 7
                return (π * r**2) + (π * r * s)
            for kerucut in range(2):
                if kerucut == 0:
                    while True :
                        a = int(input("Masukkan Jari-Jari  Kerucut :"))
                        if a <=0:
                            print("Maaf Masukkan angka Positif!!")
                        else:
                            break
                        b = int(input("Masukkan Luas Selimut Tabung Kerucut :"))
                        if b <=0:
                            print("Maaf Masukkan angka Positif!!")
                        else:
                            break
            jumlah = hitung_luas_kerucut(b, a)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Luas Permukaan Kerucut adalah = (π ˟ ({a}˟{a}))˟{b}={jumlah}cm²')
        elif pilihan == "2" :
            def hitung_volume_kerucut(r,t):
                π = 22 / 7
                return  1/3 * π * r**2 * t
            for kerucut in range(2):
                if kerucut == 0:
                    while True:
                        a = int(input("Masukkan Jari-Jari  Kerucut :"))
                        if a <= 0:
                            print("Maaf Masukkan angka Positif!!")
                        else:
                            break
                        b = int(input("Masukkan Luas Selimut Tabung Kerucut :"))
                        if b <= 0:
                            print("Maaf Masukkan angka Positif!!")
                        else:
                            break
            jumlah = hitung_volume_kerucut(a,b)
            cn = int(input("Bisa menebak hasilnya berapa?"))
            (tebak(cn))
            print(f'Volume Kerucut adalah = (1/3 ˟ π ˟ ({a**2}))˟{b}={jumlah}cm³')
        else:
            print("Salah Input")
    elif bangun_pilihan == "5":
        end = "TERIMAKASIH TELAH MENCOBA"
        print(end.center(50, "="))
        break
    else:
        print('KODE SALAH!!')
    validasi = input('Ada yang ingin dihitung kembali ?[Y/N]')
    if validasi == "Y" or validasi =="y":
        print(qwe)
        continue
    else:
        end = "TERIMAKASIH TELAH MENCOBA"
        print(end.center(50, "="))
        break