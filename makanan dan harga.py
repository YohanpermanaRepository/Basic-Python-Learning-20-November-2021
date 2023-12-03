print("Masukkan data makanan dan harga")
print("=" * 28)
makanan = []
harga = []
i = 0

for i in range (5) :
    menu = input("Masukkan nama makanan : ")
    makanan.append(menu)
    harga_menu = int(input("Harga : "))
    harga.append(harga_menu)

print("")
print("=" * 21)
print("Makanan yang tersedia")
print("=" * 21)

for cetak_menu in range (len(makanan) and len(harga)):
    print("=> Menu", makanan[cetak_menu], "dengan harga", harga[cetak_menu])