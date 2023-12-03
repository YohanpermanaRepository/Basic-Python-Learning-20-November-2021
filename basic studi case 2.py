# YOHAN PERMANA (210441100052) 

dict_status = {"Nama": "cat", "Status": "Bayi", "Power": 0 }
usia = 0
print("")

def olahraga():
    dict_status["Power"] = dict_status["Power"] - 100
    global usia

def makan():
    dict_status["Power"] = dict_status["Power"] + 100
    global usia

    usia = usia + 50
    
    if usia < 200:
        dict_status["Status"] = "Bayi"
    elif usia >= 200 and usia < 300:
        dict_status["Status"] = "Remaja"
    else:
        dict_status["Status"] = "Dewasa"

x = 0
while x == 0:
    try:
        print("1. Kasih Makan\n2. Lihat Status\n3. Ajak Olahraga\n4. Selesai")
        input1 = int(input("Mau Di Apakan Kucingmu... ?? "))
        print("")
        if input1 == 1:
            makan()
            print("nyam... nyam... nyam...\n")
        elif input1 == 2:
            print(dict_status,"\n")
        elif input1 == 3:
            olahraga()
            print(" saya sehat !! \n")
        elif input1 == 4:
            print("Terima Kasih sudah merawat Kucingmu\n")
            x = 1
        else:
            print("Maaf yang anda masukkan salah salahh!!\n")
    except ValueError:
        print("\n Masukkan kembali dengan benar yakni angka!!\n")

