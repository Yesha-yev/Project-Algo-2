# import pandas as pd # import file csv
# import os #(untuk clear terminal)
# import getpass #supaya si password tidak kelihatan
# import Login as log

# status_login = False
# def clear_terminal():
#     # Clear terminal screen
#     os.system('cls' if os.name == 'nt' else 'clear')
# def bacafile(file = "Data_login.csv"):
#     # membaca file csv
#     try:
#         return pd.read_csv(file)
#     except FileNotFoundError:
#         print(f"File {file} tidak ditemukan")
#         return pd.DataFrame(columns=["username","password"])
    
# def login():
#     global status_login
#     data=bacafile()
#     while True:
#         username = input("Masukkan username kamu : ").strip()
#         password = getpass.getpass("Masukkan Password kamu : ").strip()
#         # Menggunakan strip untuk menghapus spasi di awal dan akhir input
#         login_match=data[(data["username"] == username) & (data["password"] == password)]
#         if not login_match.empty:
#             status_login = True
#             print("Login berhasil!")
#             break
#         else:
#             print("Login gagal: Username atau password salah")
#             coba_lagi = input("Apakah kamu ingin mencoba lagi? (y/n): ").strip().lower()
#             if coba_lagi != 'y':
#                 break
# def logout():
#     global status_login
#     status_login = False
#     print("Anda telah berhasil logout.")

# def menu_tampilan():
#     clear_terminal()
#     print(
# """
# ╔══════════════════╗
# ║  Selamat Datang  ║
# ║┌────────────────┐║
# ║│  1. Login      │║
# ║│  2. Logout     │║    
# ║├────────────────┤║
# ║│   Login Page   │║
# ║└────────────────┘║
# ╚══════════════════╝
# """)

# def menu():
#     menu_tampilan()
#     while True:
#         pilihan = input("Pilih menu (1/2): ").strip()
#         if pilihan == '1':
#             clear_terminal()
#             login()
#             if status_login:
#                 print("Anda telah berhasil login.")
#                 break
#         elif pilihan == '2':
#             clear_terminal()
#             logout()
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")
#             continue
