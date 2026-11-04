import os
from data import user
from fungsi_umum import tekan_enter, tanya_teks, tanya_password

def register():
    os.system('cls')
    print("=== REGISTER ===")
    username_baru = tanya_teks("Masukkan Username Baru")
    password_baru = tanya_password("Masukkan Password Baru")
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
        username = tanya_teks("Username")
        password = tanya_password("Password")
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