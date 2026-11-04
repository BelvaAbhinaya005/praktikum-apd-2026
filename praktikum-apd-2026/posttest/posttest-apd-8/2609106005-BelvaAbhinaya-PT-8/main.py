import os
from autentikasi import login, register
from crud import (tambah_pengeluaran, lihat_pengeluaran, filter_kategori,
                  ubah_pengeluaran, hapus_pengeluaran)
from fungsi_umum import ambil_data_tampil, tanya_pilihan

def menu_user(user_aktif, role):
    while True:
        os.system('cls')
        print(f"=== MENU {role.upper()} - {user_aktif} ===")
        menu = tanya_pilihan("Pilih menu", [
            "Tambah Pengeluaran",
            "Lihat Semua Pengeluaran",
            "Filter & Total per Kategori",
            "Ubah Pengeluaran",
            "Hapus Pengeluaran",
            "Logout"
        ])

        data_tampil = ambil_data_tampil(user_aktif, role)

        if menu == "Tambah Pengeluaran":
            tambah_pengeluaran(user_aktif)
        elif menu == "Lihat Semua Pengeluaran":
            lihat_pengeluaran(data_tampil)
        elif menu == "Filter & Total per Kategori":
            filter_kategori(data_tampil)
        elif menu == "Ubah Pengeluaran":
            ubah_pengeluaran(data_tampil)
        elif menu == "Hapus Pengeluaran":
            hapus_pengeluaran(data_tampil)
        else:
            break

def main():
    laman = True
    while laman:
        os.system('cls')
        print("=== SISTEM PENCATAT KEUANGAN HARIAN ===")
        pilihan = tanya_pilihan("Pilih Menu", ["Login", "Register", "Keluar"])

        if pilihan == "Login":
            user_aktif, role = login()
            if user_aktif != "":
                menu_user(user_aktif, role)
        elif pilihan == "Register":
            register()
        else:
            print("Terima kasih!")
            laman = False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program dihentikan paksa.")
    finally:
        print("Program selesai.")