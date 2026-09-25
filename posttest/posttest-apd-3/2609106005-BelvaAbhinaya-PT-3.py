nama= input("Masukkan Nama : ")
umur = int(input("Masukan Umur : "))    

if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")   
else:
    jenis_tiket = input("Pilih Jenis Tiket (reguler / premium / vip): ")
    if jenis_tiket == "reguler":
        harga_tiket = 50000
        status = True
    elif jenis_tiket == "premium":
        harga_tiket = 75000
        status = True
    elif jenis_tiket == "vip":
        harga_tiket = 100000
        status = True
    else:
        print("Jenis Tiket Tidak Valid")
        status = False
    
    if status == True:
        status_member = input("Apakah Memiliki Member (ya / tidak) : ")
        nominal_diskon = harga_tiket*0.2 if status_member == "ya" else 0
        biaya_admin = 0 if status_member == "ya" else 2000
        total_bayar = harga_tiket - nominal_diskon + biaya_admin
        print("Total Bayar : ",total_bayar)
        nominal_uang_bayar = int(input("Masukkan Nominal Uang Anda : "))
        if nominal_uang_bayar < total_bayar:
            print("Uang Tidak Cukup")
        else:
            kembalian = nominal_uang_bayar - total_bayar
            print("_______________________")
            print("    Struk Pembelian")
            print("_______________________")
            print("Nama          :",nama)
            print("Umur          :",umur)
            print("Jenis Tiket   :",jenis_tiket)
            print("Status Member :",status_member)
            print("Total Bayar   : Rp.",total_bayar)
            print("Kembalian     : Rp.",kembalian)
    