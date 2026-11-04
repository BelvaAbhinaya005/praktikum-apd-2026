import matplotlib.pyplot as plt

# # Menginisiasi nilai pada sumbu x,y dan y2
# x = [1, 2, 3, 4, 5]
# y = [10, 35, 20, 70, 60]
# y2 = [12, 43, 56, 23, 67]

# # Inisialisasi kanvas
# plt.figure(figsize=(8, 4))

# # plt.plot() untuk masing-masing garis
# plt.plot(x, y, marker="o", color="blue", label="Matematika")
# plt.plot(x, y2, color="red", marker="h", linestyle="--", label="Fisika")

# # Detail elemen untuk memambahkan teks
# plt.title("grafik")
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu Y")
# plt.grid(True)
# plt.show()




# # Data
# jurusan = ["Informatika", "Sistem Informasi", "Teknik Elektro"]
# jumlah_mahasiswa = [120, 90, 75]

# # Membuat bar chart
# plt.bar(jurusan, jumlah_mahasiswa, color = ["Merah","Biru","Hijau"])

# # Menambahkan judul dan label
# plt.title("Jumlah Mahasiswa Berdasarkan Jurusan")
# plt.xlabel("Jurusan")
# plt.ylabel("Jumlah Mahasiswa")

# # Menampilkan grafik
# plt.show()




# import matplotlib.pyplot as plt

# # Data jam belajar dan nilai mahasiswa
# jam_belajar = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9]
# nilai = [55, 60, 65, 63, 70, 72, 78, 75, 82, 80, 88, 85, 90, 92, 95]

# # Membuat scatter plot
# plt.scatter(jam_belajar, nilai)

# # Menambahkan judul dan label
# plt.title("Hubungan Jam Belajar dengan Nilai Mahasiswa")
# plt.xlabel("Jam Belajar (Jam)")
# plt.ylabel("Nilai")

# # Menampilkan grafik
# plt.show()



import matplotlib.pyplot as plt

# Data nilai mahasiswa
nilai = [
    65, 70, 72, 75, 78,
    80, 82, 85, 88, 90,
    92, 95, 76, 83, 98,
    30, 87, 89, 73, 100
]

# Membuat box plot
plt.boxplot(nilai)

# Menambahkan judul dan label
plt.title("Distribusi Nilai Ujian Mahasiswa")
plt.ylabel("Nilai")

# Menampilkan grafik
plt.show()