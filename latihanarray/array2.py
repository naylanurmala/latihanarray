# Deklarasi matris pertama dan kadua
matriks1 = []
matriks2 = []

# Meminta input untuk matriks pertama
print("Masukkan elemen untuk matriks pertama:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}:"))
        baris.append(nilai)
    matriks1.append(nilai)
    
# Meminta input untuk matriks kedua
print("\nMasukkan elemen untuk matriks kedua:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}:"))
        baris.append(nilai)
    matriks2.append(baris)
    
# Penumlahan matriks
hasil = []
for i in range(2):
    baris = []
    for j in range(2):
        baris.append(matriks1[i][j] + matriks2[i][j])
    hasil.append(baris)
    
# menampilkan hasil penjumlahan
print("\nhasil oenjumlahan matriks:")
for bari in hasil:
    print(baris)