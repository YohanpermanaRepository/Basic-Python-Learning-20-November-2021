
mk= set()
pk=set ()

user = int(input("Ana di minggu pertama kuliah mendapatkan berapa tugas matakuliah : " ))

for i in range(user):
    input1 = (mk.add(input("Tugas mata kuliah yang didapatkan ana :")))  
print("-"*100)
print (mk)
print("-"*100)

user = int(input("Ana di minggu pertama kuliah mendapatkan berapa praktikum : " ))

for i in range(user):
    input1 = (pk.add(input("Tugas praktikum yang didapatkan ana :")))  
print("-"*100)
print (pk)
print("-"*100)

print ("Jadi tugas yang didapatkan ana pada minggu pertama kuliah adalah ")
print(mk.union(pk))
print()

print("Setelah seminggu ana menyelesaikan tugas.\n")
user1 = int(input("berapa tugas matkul yang sudah dikumpulkan : "))

for i in range(user1):
    ts= input(f" Masukkan tugas matkul yang sudah dikumpulkan  : ")
    mk.remove(ts)
print("\n Maka sisa tugas matkul ana adalah : ", mk)
print()

user2 = int(input("berapa tugas praktikum yang sudah dikumpulkan : "))

for i in range(user2):
    ps= input(f" Masukkan tugas praktikum yang sudah dikumpulkan  : ")
    pk.remove(ps)
print("\n Maka sisa tugas praktikum ana adalah : ", pk)
print()
print("sisa semua tugas ana saat ini ")
print(mk.union(pk))
print()

user3 = int(input("diminggu ketiga kuliah mendapatkan berapa tugas matakuliah : " ))

for i in range(user3):
    input1 = (mk.add(input("Tugas mata kuliah yang didapatkan ana :")))  
print("-"*100)
print (mk)
print("-"*100)

user3 = int(input("diminggu ketiga kuliah mendapatkan berapa tugas praktikum : " ))

for i in range(user3):
    input1 = (pk.add(input("Tugas praktikum yang didapatkan ana :")))  
print("-"*100)
print (pk)
print("-"*100)

user1 = int(input("berapa tugas matkul yang sudah dikumpulkan : "))

for i in range(user1):
    ts= input(f" Masukkan tugas matkul yang sudah dikumpulkan  : ")
    mk.remove(ts)
print("\n Maka sisa tugas matkul ana adalah : ", mk)
print()

user2 = int(input("berapa tugas praktikum yang sudah dikumpulkan : "))

for i in range(user2):
    ps= input(f" Masukkan tugas praktikum yang sudah dikumpulkan  : ")
    pk.remove(ps)
print("\nMaka sisa tugas praktikum ana adalah : ", pk)
print()
print("sisa semua tugas ana saat ini ")
print(mk.union(pk))
print()

user4 = int(input("Di minggu keempat kuliah mendapatkan berapa tugas matakuliah : " ))

for i in range(user4):
    input1 = (mk.add(input("Tugas mata kuliah yang didapatkan ana :")))  
print("-"*100)
print (mk)
print("-"*100)

user4 = int(input("Di minggu keempat kuliah mendapatkan berapa tugas praktikum : " ))

for i in range(user4):
    input1 = (pk.add(input("Tugas praktikum yang didapatkan ana :")))  
print("-"*100)
print (pk)
print("-"*100)

user1 = int(input("berapa tugas matkul yang sudah dikumpulkan : "))

for i in range(user1):
    ts= input(f" Masukkan tugas matkul yang sudah dikumpulkan  : ")
    mk.remove(ts)
print("\n Maka sisa tugas matkul ana adalah : ", mk)
print()

user2 = int(input("berapa tugas praktikum yang sudah dikumpulkan : "))

for i in range(user2):
    ps= input(f" Masukkan tugas praktikum yang sudah dikumpulkan  : ")
    pk.remove(ps)

print("\nMaka sisa tugas praktikum ana adalah : ", pk)

print ("Jadi tugas yang belum dikumpulkan ana pada minggu pertama sampai keempat kuliah adalah ")
print(mk.union(pk))