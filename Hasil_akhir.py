import pandas as pd
import Login as log
from tabulate import tabulate as tb

def dashboard(pengguna):
    print('''
    Halo Selamat Datang!!
    saat ini ada ..... jumlah lahan''')
    print(
"""
╔══════════════════════════════╗
║        Dashboard Pengguna    ║
║┌────────────────────────────┐║
║│  1. Input Data Lahan &     │║
║│     Tanaman                │║
║│  2. Integrasi Harga Pupuk  │║
║│  3. Kalkulasi Kebutuhan    │║
║│     Nutrisi                │║
║│  3. Simulasi Biaya Pupuk   │║
║│     Hemat                  │║
║│  4. Hitung Kebutuhan Bibit │║
║│     setiap Lahan           │║
║│  4. Tampilan Rekomendasi   │║
║├────────────────────────────┤║
║│  5. Keluar                 │║
║└────────────────────────────┘║
╚══════════════════════════════╝
""")
