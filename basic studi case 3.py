# YOHAN PERMANA (210441100052)
# /// Union
# Membuat set x dan y :
x = {1, 2, 3, 4, 5} 
y = {4, 5, 6, 7, 8}
# Gabungan menggunakan operator |
print("union : ", (x | y ))
print(" ")
# Intersecsion
x = {1, 2, 3, 4, 5} 
y = {4, 5, 6, 7, 8}
# Irisan dengan operator &
print("intersection : ", (x & y))
x.intersection(y)
y.intersection(x)
print(" ")
# Selisih membuat x dan y
x = {1, 2, 3, 4, 5} 
y = {4, 5, 6, 7, 8}
# Menggunakan operator
print("Selisih : ", (x-y))
x.difference(y)
print("Selisih : ", (y-x))
