import pandas as pd
import Login as log
from tabulate import tabulate as tb

def dashboard(pengguna):
    print(
"""
╔══════════════════════════════╗
║        Dashboard Pengguna    ║
║┌────────────────────────────┐║
║│  1. Perhitungan Kebutuhan  │║
║│     Bibit                  │║
║│  2. History Panen          │║
║│  3. Manajemen Data Tanaman │║
║│  4. Manajemen Lahan        │║
║├────────────────────────────┤║
║│  5. Keluar                 │║
║└────────────────────────────┘║
╚══════════════════════════════╝
""")
