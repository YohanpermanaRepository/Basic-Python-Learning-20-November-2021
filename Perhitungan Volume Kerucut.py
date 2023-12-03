# Nama : Yohan Permana 
# Nim  : 210441100052

# Menghitung Volume Kerucut

print("Menghitung volume kerucut") 

print("Hitung jari-jari")
ls=float(input("masukkan nilai luas selimut "))
s=float(input("masukkan garis pelukis kerucut"))
pi = 3.14

r=ls/(pi*s)
print("jadi jari-jari pada kerucut =", r, " selanjutnya adalah =")
t = float(input("masukkan tinggi kerucut = "))
v = (pi*(r**2)*t)/3

#Cetak nilai akhir 
print("jadi volume kerucut tersebut adalah ",v/1000)