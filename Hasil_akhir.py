import csv
# from tabulate import tabulate as tb

# def dashboard(pengguna):
#     print('''
#     Halo Selamat Datang!!
#     saat ini ada ..... jumlah lahan''')
#     print(
# """
# ╔══════════════════════════════╗
# ║        Dashboard Pengguna    ║
# ║┌────────────────────────────┐║
# ║│  1. Input Data Lahan &     │║
# ║│     Tanaman                │║
# ║│  2. Integrasi Harga Pupuk  │║
# ║│  3. Kalkulasi Kebutuhan    │║
# ║│     Nutrisi                │║
# ║│  3. Simulasi Biaya Pupuk   │║
# ║│     Hemat                  │║
# ║│  4. Hitung Kebutuhan Bibit │║
# ║│     setiap Lahan           │║
# ║│  4. Tampilan Rekomendasi   │║
# ║├────────────────────────────┤║
# ║│  5. Keluar                 │║
# ║└────────────────────────────┘║
# ╚══════════════════════════════╝
# """)
def bacafile(file):
    data = []  # Inisialisasi sebagai list bukan dictionary
    try:
        with open(file, mode='r', newline='') as filename:
            reader = csv.DictReader(filename)
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError:
        print(f"File {file} tidak ditemukan")
    return data

    
def greedy(dapuk,uang=None):
    hasil=[]
    for itm in dapuk:
        itm["nitrogen(gram)"] = int(itm["nitrogen(gram)"])
        itm["efektif"] = int(itm["efektif"])
        itm["harga(gram)"] = int(itm["harga(gram)"])

    # for itm in dapuk:
        # itm["nitrogen(gram)"] = int(itm["nitrogen(gram)"])
        itm["efisien"]=itm["efektif"]/itm["nitrogen(gram)"]

    dapuk.sort(key=lambda x: x["efisien"],reverse=True)
    # print(f"ini ya {dapuk}")
    nilai_efektif=0
    itm_pilih=[]
    total_nitrogen=0
    total_harga = 0

    if kebutuhan is not None:
        sisa=kebutuhan
        for p in 



tanaman = bacafile("Manajemen_data_tanaman.csv")
pupuk=bacafile("Pupuk.csv")

namatanaman

    
#     print('''
# ╔══════════════════════════════╗
# ║        Silahkan Memilih      ║
# ║┌────────────────────────────┐║
# ║│  1. Sesuai Kebutuhan       │║
# ║│  2. Sesuai Budget yang     │║
# ║│     Dimiliki               │║
# ║└────────────────────────────┘║
# ╚══════════════════════════════╝

#     ''')
#     pilihan = int(input("Masukkan pilihan anda : "))
#     if pilihan == 1:
#         tumbuhan = input("Masukkan Jenis Tumbuhan yang ingin ditanam (ex:cabai) : ")
#         for itm in dapuk:
#             if itm["nitrogen(gram)"] <= sisa:
#                 total = itm["harga(gram)"] * itm["nitrogen(gram)"]
#                 sisa-=itm["nitrogen(gram)"]
#                 nilai_efektif+=itm["efektif"]
#                 total_harga += total
#                 itm_pilih.append(
#                     {
#                         "nama": itm["nama"],
#                         "kebutuhan_nitrogen": itm["nitrogen(gram)"],
#                         "efektif": itm["efektif"],
#                         "harga": total
#                 })
#         return nilai_efektif,itm_pilih,total_harga
#     elif pilihan == 2:
#         kebutuhan =int(input("Masukkan angka : "))
#         if uang is None or uang <=0:
#             print("Uang tidak boleh kosong atau 0")
#             return 0, [],0
#         for itm in dapuk:
#             total = itm["harga(gram)"] * itm["nitrogen(gram)"]
#             if itm["nitrogen(gram)"] <= sisa and total_harga + total <= uang:
#                 sisa -= itm["nitrogen(gram)"]
#                 nilai_efektif += itm["efektif"]
#                 total_harga += total
#                 itm_pilih.append({
#                     "nama": itm["nama"],
#                     "kebutuhan_nitrogen": itm["nitrogen(gram)"],
#                     "efektif": itm["efektif"],
#                     "harga": total
#                 })
#         return nilai_efektif, itm_pilih, total_harga
#     else:
#         print("Tidak Valid")
#         return 0, [], 0
#     # return nilai_efektif, itm_pilih, total_harga


# dapuk = bacafile("Manajemen_data_tanaman.csv")
# uang = int(input("Masukkan Jumlah Uang yang kamu miliki : "))
# nilai_max,total = greedy(dapuk,uang)
# print(f"Total nilai_efektif efektif : {nilai_max}. Dan uang yang harus dikeluarkan : {total}")
# print("Pupuk yang terpilih : ")
# for i,pupuk in enumerate(terpilih, start=1):
#     print(f"{i}.{pupuk['nama']} - Kebutuhan Nitrogen: {pupuk['kebutuhan_nitrogen']} gram, Efektif: {pupuk['efektif']}, Harga: {pupuk['harga']}")