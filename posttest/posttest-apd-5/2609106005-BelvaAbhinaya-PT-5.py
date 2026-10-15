import os

user = [
    ["admin", "admin123", "admin"],
    ["belva", "belva005", "user"]
]

pengeluaran = []

kategori = ("ATK", "Makanan", "Transportasi", "Hiburan", "Lainnya")

laman = True 
while laman == True:
    os.system('cls')
    print("=== SISTEM PENCATAT KEUANGAN HARIAN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih Menu: ")

    if pilihan == "2":
        os.system('cls')
        print("=== REGISTER ===")
        username_baru = input("Masukkan Username Baru: ")
        password_baru = input("Masukkan Password Baru: ")
        ada = False
        for u in user :
            if u[0] == username_baru:
                ada = True
        if username_baru == "":
            print("Username Tidak Boleh Kosong")
        elif ada == True:
            print ("Username Sudah Terpakai")
        elif len(password_baru) < 4:
            print("Password Minimal 4 Karakter")
        else :
            user.append([username_baru, password_baru, "user"])
            print("Register berhasil! Silakan login.")
        input("Tekan Enter Untuk Lanjut...")

    elif pilihan == "1":
        percobaan = 0 
        berhasil = False
        user_aktif = ""
        role = ""

        while percobaan < 3 and berhasil == False:
            os.system('cls')
            print("=== LOGIN ===")
            username = input("Username: ")
            password = input("Password: ")

            for u in user:
                if u[0] == username and u[1] == password:
                    berhasil = True
                    user_aktif = u[0]
                    role = u[2]
                    print("Login Berhasil")
                    input("Tekan Enter Untuk Lanjut...")
                    break

            if berhasil == False:
                percobaan += 1
                print(f"Username/password salah! Sisa percobaan: {3 - percobaan}")
                input("Tekan Enter untuk lanjut...")

        login = berhasil
        if not berhasil:
            print("Gagal login 3 kali, kembali ke menu awal.")
            input("Tekan Enter untuk lanjut...")

        while login:
            os.system('cls')
            print(f"=== MENU {role.upper()} - {user_aktif} ===")
            print("1. Tambah Pengeluaran")
            print("2. Lihat Semua Pengeluaran")
            print("3. Filter & Total per Kategori")
            print("4. Ubah Pengeluaran")
            print("5. Hapus Pengeluaran")
            print("6. Logout")
            menu = input("Pilih menu: ")

            data_tampil = []
            for i in range(len(pengeluaran)):
                if role == "admin" or pengeluaran[i][0] == user_aktif:
                    data_tampil.append(i)

            if menu == "1":
                os.system('cls')
                print("=== TAMBAH PENGELUARAN ===") 

                valid = False
                while valid ==  False:
                    tanggal = input("Tanggal (DD-MM-YYYY): ")
                    bagian = tanggal.split("-")
                    if len(bagian) == 3:
                        if bagian[0].isdigit() and bagian[1].isdigit() and bagian[2].isdigit():
                            if len(bagian[0]) == 2 and len(bagian[1]) == 2 and len(bagian[2]) == 4:
                                hari = int(bagian[0])
                                bulan = int(bagian[1])
                                tahun = int(bagian[2])
                                if 1 <= hari <= 31 and 1 <= bulan <= 12 and tahun >= 2026:
                                    valid = True
                    if not valid:
                        print("Tanggal tidak valid! Contoh: 14-10-2026")

                valid = False
                while not valid:
                    nominal = input("Nominal (angka): ")
                    if nominal.isdigit() and int(nominal) > 0:
                        valid = True
                    else:
                        print("Nominal harus angka lebih dari 0!")

                valid = False
                while not valid:
                    catatan = input("Catatan: ")
                    if catatan != "":
                        valid = True
                    else:
                        print("Catatan tidak boleh kosong!")

                print("Kategori:")
                for i in range(len(kategori)):
                    print(f"{i + 1}. {kategori[i]}")
                valid = False
                while not valid:
                    pilihkategori = input("Pilih kategori: ")
                    if pilihkategori.isdigit() and 1 <= int(pilihkategori) <= len(kategori):
                        valid = True
                    else:
                        print("Pilihan kategori tidak valid!")
                    
                pengeluaran.append([user_aktif, tanggal, int(nominal), catatan, kategori[int(pilihkategori) - 1]])
                print("Data berhasil ditambahkan!")
                input("Tekan Enter untuk lanjut...")

            elif menu == "2":
                os.system('cls')
                print("=== RIWAYAT PENGELUARAN ===")
                if len(data_tampil) == 0:
                    print("Belum ada data.")
                else:
                    total = 0
                    for no in range(len(data_tampil)):
                        d = pengeluaran[data_tampil[no]]
                        print(f"{no + 1}. {d[1]} | {d[4]} | Rp {d[2]} | {d[3]} | oleh {d[0]}")
                        total += d[2]
                    print(f"Total keseluruhan: Rp {total}")
                input("Tekan Enter untuk lanjut...")
            
            elif menu == "3":
                os.system('cls')
                print("=== FILTER PER KATEGORI ===")
                for i in range(len(kategori)):
                    print(f"{i + 1}. {kategori[i]}")
                pilihkategori = input("Pilih kategori: ")
                if pilihkategori.isdigit() and 1 <= int(pilihkategori) <= len(kategori):
                    filterkategori = kategori[int(pilihkategori) - 1]
                    total = 0
                    jumlah = 0
                    print(f"\nPengeluaran kategori {filterkategori}:")
                    for idx in data_tampil:
                        d = pengeluaran[idx]
                        if d[4] == filterkategori:
                            jumlah += 1
                            print(f"{jumlah}. {d[1]} | Rp {d[2]} | {d[3]} | oleh {d[0]}")
                            total += d[2]
                    if jumlah == 0:
                        print("Tidak ada data pada kategori ini.")
                    else:
                        print(f"Total {filterkategori}: Rp {total}")
                else:
                    print("Pilihan kategori tidak valid!")
                input("Tekan Enter untuk lanjut...")

            elif menu == "4":
                os.system('cls')
                print("=== UBAH PENGELUARAN ===")
                if len(data_tampil) == 0:
                    print("Belum ada data.")
                else:
                    for no in range(len(data_tampil)):
                        d = pengeluaran[data_tampil[no]]
                        print(f"{no + 1}. {d[1]} | {d[4]} | Rp {d[2]} | {d[3]} | oleh {d[0]}")
                    nomor = input("Pilih nomor data yang diubah: ")
                    if nomor.isdigit() and 1 <= int(nomor) <= len(data_tampil):
                        idx = data_tampil[int(nomor) - 1]
                        print("1. Ubah nominal")
                        print("2. Ubah kategori")
                        print("3. Ubah catatan")
                        ubah = input("Pilih yang diubah: ")

                        if ubah == "1":
                            nominal = input("Nominal baru: ")
                            if nominal.isdigit() and int(nominal) > 0:
                                pengeluaran[idx][2] = int(nominal)
                                print("Nominal berhasil diubah!")
                            else:
                                print("Nominal harus angka lebih dari 0!")
                        elif ubah == "2":
                            for i in range(len(kategori)):
                                print(f"{i + 1}. {kategori[i]}")
                            pk = input("Pilih kategori baru: ")
                            if pk.isdigit() and 1 <= int(pk) <= len(kategori):
                                pengeluaran[idx][4] = kategori[int(pk) - 1]
                                print("Kategori berhasil diubah!")
                            else:
                                print("Pilihan kategori tidak valid!")
                        elif ubah == "3":
                            catatan = input("Catatan baru: ")
                            if catatan != "":
                                pengeluaran[idx][3] = catatan
                                print("Catatan berhasil diubah!")
                            else:
                                print("Catatan tidak boleh kosong!")
                        else:
                            print("Pilihan tidak valid!")
                    else:
                        print("Nomor tidak valid!")
                input("Tekan Enter untuk lanjut...")

            elif menu == "5":
                os.system('cls')
                print("=== HAPUS PENGELUARAN ===")
                if len(data_tampil) == 0:
                    print("Belum ada data.")
                else:
                    for no in range(len(data_tampil)):
                        d = pengeluaran[data_tampil[no]]
                        print(f"{no + 1}. {d[1]} | {d[4]} | Rp {d[2]} | {d[3]} | oleh {d[0]}")
                    nomor = input("Pilih nomor data yang dihapus: ")
                    if nomor.isdigit() and 1 <= int(nomor) <= len(data_tampil):
                        yakin = input("Yakin hapus? (y/n): ")
                        if yakin == "y" or yakin == "Y":
                            del pengeluaran[data_tampil[int(nomor) - 1]]
                            print("Data berhasil dihapus!")
                        else:
                            print("Penghapusan dibatalkan.")
                    else:
                        print("Nomor tidak valid!")
                input("Tekan Enter untuk lanjut...")

            elif menu == "6":
                login = False

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk lanjut...")

    elif pilihan == "3":
        print("Terima kasih!")
        laman = False

    else:
        print("Menu tidak valid!")
        input("Tekan Enter untuk lanjut...")





