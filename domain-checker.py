import socket
from os import system
from os import chdir
from colorama import Fore
import keyboard

sil = lambda: system("cls")
red = Fore.RED
dark = Fore.LIGHTBLACK_EX

def check_domain_availability(domain):
    try:
        socket.gethostbyname(domain)
        return False  
    except socket.gaierror:
        return True

def main():
    print("{}Doğruluyacağınız Domaini Giriniz:{}".format(red, dark))
    domains = input().split(",")
    domains = [domain.strip() for domain in domains]

    print("\n{}Sonuçlar:{}".format(red, dark))
    for domain in domains:
        if check_domain_availability(domain):
            print(f"{domain} -> Boşta")
            anamenu2 = input("\n{} Yeni Sorgu İçin {}+{}, geri dönmek için {}-".format(red, dark, red, dark))
            if anamenu2 == ("+"):
                sil()
                main()
            elif anamenu == ("-"):
                sil()
                chdir("..")
                chdir("..")
                system("python multitool.py")
        else:
            print(f"{domain} -> Meşgül")
            anamenu = input("\n{} Yeni Sorgu İçin {}+{}, geri dönmek için {}-".format(red, dark, red, dark))
            if anamenu == ("+"):
                sil()
                main()
            elif anamenu == ("-"):
                sil()
                chdir("..")
                chdir("..")
                system("python multitool.py")
if __name__ == "__main__":
    main()
