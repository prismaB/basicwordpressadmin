import requests
import sys
from colorama import Fore,Back,Style,init
import time
init(autoreset=True)

target = sys.argv[1]
def scanstart():
    import subprocess
    subprocess.call("clear")
    print("check network")
    check = 'https://github.com'
    r = requests.get(check)
    if r.status_code == 200 or r.status_code == 404 or r.status_code == 302:
        print("check completed")
    else:
        try:
            sys.exit()
        except:
            pass
    ad = requests.get("http://" + target + " " + "/admin")
    if ad.status_code == 200:
        print(Fore.Green + " found /admin => code 200")
    if ad.status_code == 403:
        print(Fore.Green + "found /admin => code 403")
    if ad.status_code == 302:
        print(Fore.Green + "found /admin code => 302")
    else:
        pass
    ad2 = requests.get("http://" + target + "/wp-admin/")
    if ad2.status_code == 200:
        print(Fore.Green + " found => /wp-admin status coce => 200")
    elif ad.status_code == 302:
        print(Fore.Green + "found => /wp-admin status code => 302")
    elif ad.status_code == 403:
        print(Fore.Green + "found => wp-admin status code 0> 403")
    else:
        pass
def animation():
    bred = Fore.RED + Style.BRIGHT
    red = Fore.RED
    bos = "\033[1;37m"
    z = """
    			        Version 1.0.0
            [+] █████████████████████████████████████████████████████ [+]
    """
    for c in z:
        sys.stdout.write(f"{bred}{c}")
        sys.stdout.flush()
        time.sleep(0.02)
def targets():
    print("options")
    print("target =>" +"  " +target)
    print("--------------------------")
    print("--------------------------")
    print("--------------------------")
    verify = input("verify [y]es or [n]o:")
    if verify == "yes" or verify == "Y" or verify == "y":
        animation()
        scanstart()
    else:
        print("err")
if __name__ == '__main__':
    targets()