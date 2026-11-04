import os
from data import pengeluaran, kategori
from fungsi_umum import (input_tanggal, input_nominal, pilih_kategori,
                      hitung_total, tekan_enter, pilih_nomor,
                      tanya_teks, tanya_pilihan)
from tampilan import tampilkan_data

id_terakhir = 0

def tambah_pengeluaran(user_aktif):
    global id_terakhir
    os.system('cls')
    print("=== TAMBAH PENGELUARAN ===")
    tanggal = input_tanggal()
    nominal = input_nominal()
    catatan = ""
    while catatan == "":
        catatan = tanya_teks("Catatan")
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
            ubah = tanya_pilihan("Pilih yang diubah",
                                 ["Ubah nominal", "Ubah kategori", "Ubah catatan"])
            if ubah == "Ubah nominal":
                pengeluaran[idx]["nominal"] = input_nominal()
                print("Nominal berhasil diubah!")
            elif ubah == "Ubah kategori":
                pengeluaran[idx]["kategori"] = pilih_kategori(kategori)
                print("Kategori berhasil diubah!")
            else:
                catatan = tanya_teks("Catatan baru")
                if catatan != "":
                    pengeluaran[idx]["catatan"] = catatan
                    print("Catatan berhasil diubah!")
                else:
                    print("Catatan tidak boleh kosong!")
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
            yakin = tanya_pilihan("Yakin hapus?", ["Ya", "Tidak"])
            if yakin == "Ya":
                del pengeluaran[idx]
                print("Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
    tekan_enter()