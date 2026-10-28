import inquirer 

 

# Menyusun daftar pertanyaan menu 
pertanyaan = [ 
    inquirer.List( 
        "menu", 
        message="Pilih menu aplikasi", 
        choices=["Tambah Data", "Lihat Data", "Keluar"], 
    ), 
] 

 

# Menampilkan prompt di terminal dan menyimpan hasil pilihan 
jawaban = inquirer.prompt(pertanyaan) 

 

print(jawaban)          # Output berupa Dictionary, misal: {'menu': 'Tambah Data'} 
print(jawaban["menu"])  # Mengambil nilai berdasarkan key 'menu': Tambah Data 

 