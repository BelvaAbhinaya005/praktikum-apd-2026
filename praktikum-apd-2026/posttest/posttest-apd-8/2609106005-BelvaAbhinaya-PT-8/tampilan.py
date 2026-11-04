from prettytable import PrettyTable
from data import pengeluaran

def tampilkan_data(data_tampil):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Tanggal", "Kategori", "Nominal", "Catatan", "User"]
    tabel.align["Catatan"] = "l"
    for no in data_tampil:
        d = pengeluaran[data_tampil[no]]
        tabel.add_row([no, d['tanggal'], d['kategori'], f"Rp {d['nominal']}", d['catatan'], d['user']])
    print(tabel)