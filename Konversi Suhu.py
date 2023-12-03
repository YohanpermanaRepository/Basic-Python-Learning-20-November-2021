# Nama : Yohan Permana
# NIM    : 210441100052

# Judul Program
print("Program konversi suhu dari Celcius ke Fahrenheit, Reanmur, dan Kelvin")

# Proses
c = int(input("Masukkan nilai Celcius yang akan di konversi : "))
f = c + 9/5 +32
r = 4/5 * c
k = c + 273

# Cetak 
print("nilai suhu", c, "derajad celcius ke dalam fahrenheit adalah : ", f)
print("nilai suhu", c, "derajad celcius ke dalam reanmur adalah : ",r)
print("nilai suhu", c, "derajad celcius ke dalam kelvin adalah : ",k)
