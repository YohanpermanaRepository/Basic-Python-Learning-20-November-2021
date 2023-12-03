kode = ['1', '2', '3', '4', '5']
menu = ['Nasi Goreng','Nasi Kuning','Nasi Pecel','Es Jeruk','Es Teh']
harga = [10000,13000,5000,4000,3000]
jurusan = ['Teknik Informatika','Teknik Industri','Teknik Elektro','Teknik Mesin','Teknik Mekatronika','Sistem Informasi']
mkn_dpsn = []
mnn_dpsn = []
jmkn_dpsn = []
jmnn_dpsn = []
H_mkn = []
H_mnn = []
JH_mkn = []
JH_mnn = []
nim = []

pilih = str(input("Masukkan NIM anda : "))
nama = str(input("Nama              : "))
nim.append(pilih)
chose = str(nim[0])
select = str(chose[3:4])
select_prodi =str(chose[3:6])
ulang = "y"
while ulang == "y" or ulang == "Y":

        print("")
        print("===========WELCOME TO KANTIN TEKNIK AREA===========")
        print("|DISKON 25% UNTUK MAHASISWA PRODI SISTEM INFORMASI|")
        print("|DISKON 10% UNTUK MAHASISWA FAKULTAS TEKNIK       |")
        print("===================================================")
        print("Ketik (y/Y) untuk setuju, (t/T) untuk batal.. ")
        pesan_mkn = input("Pesan makan? ")
        if pesan_mkn == "y" or pesan_mkn == "Y":
            mkn = "y"
            while mkn == "y" or mkn == "Y":
                print("==========================================")
                print(" MENU MAKANAN: ")
                print("==========================================")
                for x in range(len(menu) and len(harga)):
                    if x <= 2 :
                        print(x+1,"=>", menu[x], "dengan harga", harga[x])
                    elif x ==  3 :
                        print("==========================================")
                        print(" MENU MINUMAN: ")
                        print("==========================================")
                        print(x+1,"=>", menu[x], "dengan harga", harga[x])
                    else :
                        print(x+1,"=>", menu[x], "dengan harga",  harga[x])
                print("")
                pilihan_mkn = input("Pilih kode Menu makanan: ")
                qty = input("Berapa banyak yang akan di beli: ")
                jmkn_dpsn.append(qty)
                i = 0
                while i < len(menu):
                    if kode[i] == pilihan_mkn:
                        nm_mkn = menu[i]
                        hrg_mkn = harga[i]
                    i += 1

                totHarMkn = hrg_mkn * int(qty)
                totHar1 = totHarMkn

                mkn_dpsn.append(nm_mkn)
                H_mkn.append(hrg_mkn)
                JH_mnn.append(totHar1)

                print("")
                print("==========================================")
                print(">>> NAMA Menu        : " + nm_mkn)
                print(">>> HARGA            : " + str(hrg_mkn))
                print(">>> JUMLAH           : " + qty)
                print(("-------------------------------"))
                print(">>> TOTAL Harga      : " + str(totHar1))
                mkn = input("Pesan makanan lagi? ")
                if mkn == "t" or mkn == "T":
                    pass

        elif pesan_mkn == "t" or pesan_mkn == "T":
            totHar1=0
            pass

        pesan_mnm = input("Pesan minum? ")
        if pesan_mnm == "y" or pesan_mnm == "Y":
            mnn = "y"
            while mnn == "y" or mnn == "Y":
                print("")
                print("==========================================")
                print(" MENU MAKANAN: ")
                print("==========================================")
                for n in range(len(menu) and len(harga)):
                    if n <= 2:
                        print(n+1,"=>", menu[n], "dengan harga", harga[n])
                    elif n == 3:
                        print("==========================================")
                        print(" MENU MINUMAN: ")
                        print("==========================================")
                        print(n+1,"=>", menu[n], "dengan harga", harga[n])
                    else:
                        print(n+1,"=>", menu[n], "dengan harga", harga[n])
                pilihan_mnm = input("Pilih kode Menu minuman: ")
                qty2 = input("Berapa banyak yang akan di beli: ")
                jmnn_dpsn.append(qty2)
                i = 0
                while i < len(menu):
                    if kode[i] == pilihan_mnm:
                        nm_mnn = menu[i]
                        hrg_mnn = harga[i]
                    i += 1

                totHarMnn = hrg_mnn * int(qty2)
                totHar2 = totHarMnn

                mnn_dpsn.append(nm_mnn)
                H_mnn.append(hrg_mnn)
                JH_mnn.append(totHar2)

                print("")
                print("==========================================")
                print(">>> NAMA Menu        : " + nm_mnn)
                print(">>> HARGA            : " + str(hrg_mnn))
                print(">>> JUMLAH           : " + qty2)
                print(("-------------------------------"))
                print(">>> TOTAL Harga      : " + str(totHar2))
                mnn = input("Pesan minuman lagi? ")
                if mnn == "t" or mnn == "T":
                    pass

        elif pesan_mnm == "t" or pesan_mnm == "T":
            totHar2 = 0
            pass

        Har1 = totHar1 and sum(H_mkn)
        Har2 = totHar2 and sum(H_mnn)

        selesai = input("Cetak tagihan pembayaran? ")
        if selesai == "y" or selesai == "Y":
            totHar = Har1 + Har2
            print("")
            print("Rincian Transaksi:")
            print("==========================================")
            print(">>> NAMA Menu         ")
            print("Makanan: ")
            print("---------------")
            for y in mkn_dpsn:
                print(y + "    || Jumlah: " + str(qty) + " || Harga tiap menu ==> " + str(totHarMkn))
            print("Minuman: ")
            print("---------------")
            for y in mnn_dpsn:
                print(y + "    || Jumlah: " + str(qty2) + " || Harga tiap menu ==> " + str(totHarMnn))
            print(("****************************************"))
            print(">>> TOTAL Harga      : Rp " + str(totHar))
            if select_prodi == "441":
                print("Prodi : ", jurusan[5])
                totHar = totHar * 75 / 100
                print("Anda mendapatkan diskon 25%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_prodi == "411":
                print("Prodi : ", jurusan[0])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_prodi == "421":
                print("Prodi : ", jurusan[1])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_prodi == "431":
                print("Prodi : ", jurusan[2])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_prodi == "451":
                print("Prodi : ", jurusan[3])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_prodi == "461":
                print("Prodi : ", jurusan[4])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            else :
                print("Anda bukan dari Fakultas Teknik")
                print("Maka anda harus membayar harga normal")
                print("==========================================")
                print(">>> TOTAL Harga : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")

        elif selesai == "t" or selesai == "T":
            pass
        print("Terimakasih Sudah Membeli di Kantin TEKNIK AREA")
        print("Datang Lagi Lain Waktu....")
        break