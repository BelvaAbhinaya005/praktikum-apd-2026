# nama = ['Andi',55, 'Budi',7.7 ,'Sinta', 'Siska']

# nama.append(7.777)
# print(nama)



# nama = ['Andi',55, 'Budi',7.7 ,'Sinta', 'Siska']

# nama.extend([False, "17 Tahun"])
# print(nama)



# nama = ['Andi',55, 'Budi',7.7 ,'Sinta', 'Siska']

# nama.insert(3, "17 Tahun")
# print(nama)


# nama = ['Andi',55, 'Budi',7.7 ,'Sinta', 'Siska']
# nama [0:2] = ['Azka','Rudi']
# print(nama)



# nama = ['Andi',55, 'Budi',7.7 ,'Sinta', 'Siska']
# del nama[2]  #by Indeks
# remove.nama('Sinta')  #By Value
# pop.nama(2)  #By Indeks


# nama = ['Andi',55, 'Budi',7.7 ,'Sinta', 'Siska']
# i = 0
# for item in nama:
#     if type(item) == str:
#         i += 1
# print (i)


# nama = ['Andi',55, 'Budi',7.7 ,'Sinta', 'Siska']
# kelas = ['A','B','C']
# print(nama + kelas)
# print(nama * 3)


# nilai = [75,70,60,50,45,44,[12,13,14,15]]
# # List Index ke-6
# print(nilai[6][2:])

# nilai = [[12, 13,[133, 132, 132, [111,112,113]]]]
# for item in nilai:
#     for j in item:
#         if isinstance(j, list):
#             for k isinstance(k,list)
#             if


# TUPLE
# hariKerja = ("Senin","Selasa","Rabu","Kamis","Jumat")
# HariKerjaList = List(hariKerja)        
# Mengubah Data HariKerja dari bentuk TUPLE Menjadi LIST (Membuat Variabel Baru Yaitu HariKerjaList)

nama = [
    "Andi", "Budi", "Citra", "Dinda", "Eko",
    "Fajar", "Adam", "Hendra", "Intan", "Joko",
    "Karin", "Lutfi", "Maya", "Nanda", "Oki",
    "Putri", "Rian", "Salsa", "Tio", "Vina",
    "Wahyu", "Yuni", "Zaki", "Alya", "Bagas",
    "Doni", "Elsa", "Farhan", "Nia", "Raka"
]

pekerjaan = [
    "Polisi", "Polisi", "Polisi", "Guru", "Petani",
    "Polisi", "Polisi", "Polisi", "Guru", "Pedagang",
    "Polisi", "Polisi", "Polisi", "Petani", "Guru",
    "Polisi", "Polisi", "Polisi", "Desainer", "Pedagang",
    "Polisi", "Polisi", "Polisi", "Dokter", "Guru",
    "Polisi", "Polisi", "Polisi", "Programmer", "Pedagang"
]

gender = [
    "Laki-laki", "Laki-laki", "Perempuan", "Perempuan", "Laki-laki",
    "Laki-laki", "Laki-laki", "Laki-laki", "Perempuan", "Laki-laki",
    "Perempuan", "Laki-laki", "Perempuan", "Laki-laki", "Laki-laki",
    "Perempuan", "Laki-laki", "Perempuan", "Laki-laki", "Perempuan",
    "Laki-laki", "Perempuan", "Laki-laki", "Perempuan", "Laki-laki",
    "Laki-laki", "Perempuan", "Laki-laki", "Perempuan", "Laki-laki"
]

umur = [
    "dewasa", "muda", "muda", "anak-anak", "dewasa",
    "muda", "muda", "dewasa", "muda", "dewasa",
    "muda", "muda", "dewasa", "muda", "anak-anak",
    "muda", "muda", "dewasa", "dewasa", "anak-anak",
    "muda", "muda", "dewasa", "dewasa", "muda",
    "muda", "dewasa", "muda", "dewasa", "dewasa"
]

bersenjata = [
    True, False, False, False, False,
    True, False, False, False, False,
    True, False, False, False, False,
    True, False, False, False, False,
    True, False, False, False, False,
    True, False, False, False, False
]

daerah = [
    "timur", "timur", "timur", "timur", "timur",
    "selatan", "selatan", "selatan", "selatan", "selatan",
    "barat", "barat", "barat", "barat", "barat",
    "utara", "utara", "utara", "utara", "utara",
    "timur", "timur", "barat", "utara", "utara",
    "barat", "utara", "timur", "selatan", "barat"
]

for i in range(len(nama)):
    if pekerjaan[i] == "Polisi" and gender[i] == "Laki-laki" and umur[i] == "muda" and daerah[i] == "selatan" and bersenjata[i] == True:
        print(nama[i])
