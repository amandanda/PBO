print("=========Prisma Segitiga=========")

sisi = [12,23,34]

tinggi = 23

luas_alas = 23

# Luas
luas_segitiga = (sisi[0] + sisi[1] + sisi[2]) * tinggi

luas_prisma = (sisi[0] + sisi[1] + sisi[2]) * 2 * luas_segitiga

# volume
volume = 1/2 * 2 * luas_alas * tinggi

# output 
print("Luas Segitiga adalah: ", luas_segitiga)
print("Luas Prisma adalah: ", luas_prisma)
print("Volumenya adalah: ", volume)