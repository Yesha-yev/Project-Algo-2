import Login as log
# import Hasil_akhir as ha

def main():
    while True :
        log.menu_tampilan()
        pilihan= input("Masukkan Inputan : ")
        match pilihan:
            case "1":
                log.login()
                if log.status_login:
                    print("Anda telah berhasil login.")
                    break
            case "2":
                log.logout()
                break
            case _:
                print("Pilihan tidak ada")

main()