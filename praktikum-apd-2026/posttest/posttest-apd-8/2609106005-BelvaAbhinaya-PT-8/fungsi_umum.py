import inquirer
from data import pengeluaran

def tanya(pertanyaan):
    jawaban = inquirer.prompt([pertanyaan])
    if jawaban is None:
        raise KeyboardInterrupt
    return jawaban["x"]

def tanya_teks(pesan):
    return tanya(inquirer.Text("x", message=pesan))

def tanya_password(pesan):
    return tanya(inquirer.Password("x", message=pesan))

def tanya_pilihan(pesan, pilihan):
    return tanya(inquirer.List("x", message=pesan, choices=pilihan))

def input_tanggal():
    while True:
        try:
            tanggal = tanya_teks("Tanggal (DD-MM-YYYY)")
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
            nominal = int(tanya_teks("Nominal (angka)"))
            if nominal <= 0:
                raise ValueError
        except ValueError:
            print("Nominal harus angka lebih dari 0!")
        else:
            return nominal

def pilih_kategori(daftar_kategori):
    return tanya_pilihan("Pilih kategori", list(daftar_kategori))

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

def pilih_nomor(data_tampil):
    pilihan = []
    for no in data_tampil:
        d = pengeluaran[data_tampil[no]]
        label = f"{no}. {d['tanggal']} | {d['kategori']} | Rp {d['nominal']} | {d['catatan']}"
        pilihan.append((label, data_tampil[no]))
    return tanya_pilihan("Pilih data", pilihan)