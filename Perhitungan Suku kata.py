
   # Nama : Yohan Permana 
# NIM  : 210441100052

# Judul Program
print("Program untuk mengetahui suku ke n dan jumlah suku ke n ")

# Perintah
n = int(input("masukan nilai yang ingin di ketahui \n = "))

# Diketahui : 
u3 = 9
u7 = 17
s3 = 3
s7 = 7

# Proses
# 1.) mencari beda dan suku pertama
q = u3 - s3
w = u7 - s7
e = (u7-u3)/(w-q)
r = u3-((s3-1)*e)

# 2.) Memasukkan ke dalam rumus
# suku yang ingin di ketahui 
s = float(r+(n-1)*e)
# jumlah dari suku pertama sampai suku yang ingin di ketahui
t = float(n/2)*(r+s)

# Cetak
print("nilai suku pertama adalah :",r)
print("nilai beda suku adalah : ", e)
# Suku yang ingin di ketahui
print("suku ke ",n, "adalah =", s)
# Jumlah dari suku pertama sampai suku yang akan di ketahui
print("jumlah suku ke" ,n, "adalah =", t) 