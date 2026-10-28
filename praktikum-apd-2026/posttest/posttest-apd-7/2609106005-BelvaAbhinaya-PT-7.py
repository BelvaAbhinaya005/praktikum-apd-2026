import os

user = {
    "admin": {"password": "admin123", "role": "admin"},
    "belva": {"password": "belva005", "role": "user"}
}
pengeluaran = {}
id_terakhir = 0
kategori = ("ATK", "Makanan", "Transportasi", "Hiburan", "Lainnya")

def input_tanggal():
    while True:
        try:
            tanggal = input("Tanggal (DD-MM-YYYY): ")
            bagian = tanggal.split("-")
            if len(bagian) != 3:
                raise ValueError
            hari = int(bagian[0])
            bulan = int(bagian[1])
            tahun = int(bagian[2])
            if not (1 <= hari <= 31 and 1 <= bulan <= 12 and tahun >= 2026):
                raise ValueError
        except ValueError:
            print("Tanggal tidak valid! Contoh: 14-10-2026")
        else:
            return tanggal

def input_nominal():
    while True:
        try:
            nominal = int(input("Nominal (angka): "))
            if nominal <= 0:
                raise ValueError

        except ValueError:
            print("Nominal harus angka lebih dari 0!")
        else:
            return nominal

def pilih_kategori(daftar_kategori):
    for i in range(len(daftar_kategori)):
        print(f"{i + 1}. {daftar_kategori[i]}")
    while True:
        try:
            pilihan = int(input("Pilih kategori: "))
            if pilihan < 1 or pilihan > len(daftar_kategori):
                raise ValueError
        except ValueError:
            print("Pilihan kategori tidak valid!")
        else:
            return daftar_kategori[pilihan - 1]

def ambil_data_tampil(user_aktif, role):
    data_tampil = {}
    nomor_urut = 1
    for id_data in pengeluaran:
        if role == "admin" or pengeluaran[id_data]["user"] == user_aktif:
            data_tampil[nomor_urut] = id_data
            nomor_urut += 1
    return data_tampil

def hitung_total(daftar_id, i):
    if i == len(daftar_id):
        return 0
    return pengeluaran[daftar_id[i]]["nominal"] + hitung_total(daftar_id, i + 1)

def tekan_enter():
    input("Tekan Enter untuk lanjut...")

def tampilkan_data(data_tampil):
    for no in data_tampil:
        d = pengeluaran[data_tampil[no]]
        print(f"{no}. {d['tanggal']} | {d['kategori']} | Rp {d['nominal']} | {d['catatan']} | oleh {d['user']}")

def pilih_nomor(data_tampil):
    try:
        nomor = int(input("Pilih nomor data: "))
        idx = data_tampil[nomor]
    except ValueError:
        print("Nomor harus berupa angka!")
        return None
    except KeyError:
        print("Nomor tidak ditemukan!")
        return None
    else:
        return idx

def register():
    os.system('cls')
    print("=== REGISTER ===")
    username_baru = input("Masukkan Username Baru: ")
    password_baru = input("Masukkan Password Baru: ")
    try:
        if username_baru == "":
            raise ValueError("Username Tidak Boleh Kosong")
        if username_baru in user:
            raise ValueError("Username Sudah Terpakai")
        if len(password_baru) < 4:
            raise ValueError("Password Minimal 4 Karakter")
    except ValueError as e:
        print(e)
    else:
        user[username_baru] = {"password": password_baru, "role": "user"}
        print("Register berhasil! Silakan login.")
    tekan_enter()

def login():
    percobaan = 0
    while percobaan < 3:
        os.system('cls')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")
        try:
            if user[username]["password"] != password:
                raise ValueError
        except (KeyError, ValueError):
            percobaan += 1
            print(f"Username/password salah! Sisa percobaan: {3 - percobaan}")
            tekan_enter()
        else:
            print("Login Berhasil")
            tekan_enter()
            return username, user[username]["role"]
    print("Gagal login 3 kali, kembali ke menu awal.")
    tekan_enter()
    return "", ""

def tambah_pengeluaran(user_aktif):
    global id_terakhir
    os.system('cls')
    print("=== TAMBAH PENGELUARAN ===")
    tanggal = input_tanggal()
    nominal = input_nominal()
    catatan = ""
    while catatan == "":
        catatan = input("Catatan: ")
        if catatan == "":
            print("Catatan tidak boleh kosong!")
    kat = pilih_kategori(kategori)

    id_terakhir += 1
    pengeluaran[id_terakhir] = {
        "user": user_aktif,
        "tanggal": tanggal,
        "nominal": nominal,
        "catatan": catatan,
        "kategori": kat
    }
    print("Data berhasil ditambahkan!")
    tekan_enter()

def lihat_pengeluaran(data_tampil):
    os.system('cls')
    print("=== RIWAYAT PENGELUARAN ===")
    if len(data_tampil) == 0:
        print("Belum ada data.")
    else:
        tampilkan_data(data_tampil)
        total = hitung_total(list(data_tampil.values()), 0)
        print(f"Total keseluruhan: Rp {total}")
    tekan_enter()

def filter_kategori(data_tampil):
    os.system('cls')
    print("=== FILTER PER KATEGORI ===")
    pilihan = pilih_kategori(kategori)
    hasil = {}
    nomor = 1
    for no in data_tampil:
        if pengeluaran[data_tampil[no]]["kategori"] == pilihan:
            hasil[nomor] = data_tampil[no]
            nomor += 1
    print(f"\nPengeluaran kategori {pilihan}:")
    if len(hasil) == 0:
        print("Tidak ada data pada kategori ini.")
    else:
        tampilkan_data(hasil)
        print(f"Total {pilihan}: Rp {hitung_total(list(hasil.values()), 0)}")
    tekan_enter()

def ubah_pengeluaran(data_tampil):
    os.system('cls')
    print("=== UBAH PENGELUARAN ===")
    if len(data_tampil) == 0:
        print("Belum ada data.")
    else:
        tampilkan_data(data_tampil)
        idx = pilih_nomor(data_tampil)
        if idx is not None:
            print("1. Ubah nominal")
            print("2. Ubah kategori")
            print("3. Ubah catatan")
            ubah = input("Pilih yang diubah: ")
            if ubah == "1":
                pengeluaran[idx]["nominal"] = input_nominal()
                print("Nominal berhasil diubah!")
            elif ubah == "2":
                pengeluaran[idx]["kategori"] = pilih_kategori(kategori)
                print("Kategori berhasil diubah!")
            elif ubah == "3":
                catatan = input("Catatan baru: ")
                if catatan != "":
                    pengeluaran[idx]["catatan"] = catatan
                    print("Catatan berhasil diubah!")
                else:
                    print("Catatan tidak boleh kosong!")
            else:
                print("Pilihan tidak valid!")
    tekan_enter()

def hapus_pengeluaran(data_tampil):
    os.system('cls')
    print("=== HAPUS PENGELUARAN ===")
    if len(data_tampil) == 0:
        print("Belum ada data.")
    else:
        tampilkan_data(data_tampil)
        idx = pilih_nomor(data_tampil)
        if idx is not None:
            yakin = input("Yakin hapus? (y/n): ")
            if yakin == "y" or yakin == "Y":
                del pengeluaran[idx]
                print("Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
    tekan_enter()

def menu_user(user_aktif, role):
    while True:
        os.system('cls')
        print(f"=== MENU {role.upper()} - {user_aktif} ===")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Semua Pengeluaran")
        print("3. Filter & Total per Kategori")
        print("4. Ubah Pengeluaran")
        print("5. Hapus Pengeluaran")
        print("6. Logout")
        menu = input("Pilih menu: ")

        data_tampil = ambil_data_tampil(user_aktif, role)

        if menu == "1":
            tambah_pengeluaran(user_aktif)
        elif menu == "2":
            lihat_pengeluaran(data_tampil)
        elif menu == "3":
            filter_kategori(data_tampil)
        elif menu == "4":
            ubah_pengeluaran(data_tampil)
        elif menu == "5":
            hapus_pengeluaran(data_tampil)
        elif menu == "6":
            break
        else:
            print("Menu tidak valid!")
            tekan_enter()

def main():
    laman = True
    while laman:
        os.system('cls')
        print("=== SISTEM PENCATAT KEUANGAN HARIAN ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            user_aktif, role = login()
            if user_aktif != "":
                menu_user(user_aktif, role)
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("Terima kasih!")
            laman = False
        else:
            print("Menu tidak valid!")
            tekan_enter()


try:
    main()
except KeyboardInterrupt:
    print("\nProgram dihentikan paksa.")
finally:
    print("Program selesai.")