username_benar = "belva"
password_benar = "005"
saldo = 5000000

login = False
for kesempatan in range(1,4):
    print("\n ******* LOGIN BANK DIGITAL ******")
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")
    if username_benar == username and password_benar == password:
        print("Login Berhasil")
        login = True
        break
    elif username_benar != username and password_benar != password:
        print("Username dan Password Anda Salah ")
    elif username_benar != username:
        print("Username Anda Salah ")
    elif password_benar != password:
        print("Password Anda Salah ")
    if kesempatan < 3:
        print("Silahkan Masukkan Kembali")
if login == False:
        print("Akun Anda Di Blokir")

if login == True:
    pilihan = ""
    while pilihan != "2" and login == True:     
        if pilihan != "1":
            print("\n ****** MENU BANK DIGITAL ******")
            print(" 1. Transfer Uang")
            print(" 2. Logout")
            print(" *******************************")
            pilihan = input(" Pilih Menu : ")
       
        elif pilihan == "1":
            print("\n ******* TRANSFER UANG *******")
            print(f" Saldo Anda : {saldo}")
            username_penerima = input(" Masuk Username Penerima : ")
            nominal_transfer = int((input)(" Nominal Transfer (50000 - 1000000): "))
            while nominal_transfer < 50000 or nominal_transfer > 1000000 or nominal_transfer > saldo:
                if nominal_transfer < 50000: 
                    print("Minimal Transfer 50000")
                    nominal_transfer = int(input(" Masukkan Kembali Nominal : "))
                elif nominal_transfer > 1000000:
                        print("Maksimal Transfer 1000000")
                        nominal_transfer = int (input(" Masukkan Kembali Nominal : "))
                elif nominal_transfer > saldo:
                        print(" SALDO ANDA TIDAK CUKUP!!")
                        nominal_transfer = int((input)(" Masukkan Kembali Nominal Transfer : ")) 
                                     
            pin_benar = "005005"
            transfer = False
            for kesempatan in range (1,4):
                pin = input(" Masukkan Pin Anda : ")
                if pin_benar == pin:
                    print(" Pin Benar, Transaksi di Proses")
                    transfer = True
                    break
                elif pin_benar != pin:
                        print(" Pin Anda Salah, Masukkan Kembali Pin Anda !!")
            if transfer == False:
                login = False
                print(" AKUN ANDA DI BLOKIR")
            elif transfer == True:
                saldo = saldo - nominal_transfer
                print(f"\n ======= Struk Bukti Transfer =======")
                print(f" Username Pengirim : {username}")
                print(f" Username Penerima : {username_penerima}")
                print(f" Nominal Transaksi : {nominal_transfer}")
                print(f"=====================================")
                    
                ulang = input("Apakah Mau Transfer Lagi (y/n)?")
                if ulang == "y":
                    pilihan = "1"
                elif ulang == "n":
                    pilihan = ""
        elif pilihan != "2":
            print("\n Pilihan Tidak Valid !!")
    if pilihan == "2" :
        print ("Anda Berhasil Log Out")